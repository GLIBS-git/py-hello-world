'''
    Collections demo Glibs Python scripts
'''
#!/usr/bin/python3
import glibs_tools
import json
import requests
import sys
import urllib3
import web_request_secrets as secrets

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    read_gtd_lines(legal_entity="RGM", gtd_id="Гтд0017612")
    #test()

def read_gtd_lines(legal_entity, gtd_id, log_files=False):
    def find_article(article_id):
        if gtd_line.get('styleLog') == article_id:
            print(" "*8, gtd_line.get('gtdLineNum'), "  ||  ", gtd_line.get('id'), "  ||  ", gtd_line.get('styleLog'))
    def incomplete_plu():
        plus: dict = gtd_line.get('PLUs')
        if plus == None or len(plus) != 3:
            print(" "*8, gtd_line.get('gtdLineNum'), "  ||  ", gtd_line.get('id'), "  ||  ", gtd_line.get('styleLog'))
            print(" "*12, json.dumps(plus, ensure_ascii=False, indent=2))
    base_url = secrets.data_ref_url() + '/gtdLines'
    headers = {}
    headers['AppKey'] = secrets.app_key(legal_entity)
    headers['ClientId'] = secrets.client_id(legal_entity)
    query_options = {}
    query_options['journalId'] = gtd_id
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Suppress the SSL warning
    page = 1
    while True:
        query_options['page'] = str(page)
        print("Reading page: ", page)
        response = requests.get(base_url, params=query_options, headers=headers, verify=False)  # Set verify=False to ignore SSL certificate warnings
        if response.status_code == 200:
            resp_json = response.json()
            if resp_json == None:
                print(" "*4, "Empty response!")
                break
            data = dict(resp_json.get('data'))
            if data == None:
                print(" "*4, "Data is empty!")
                break
            print(" "*4, "Lines on page: ", data.get('pageSize'))
            gtd_lines = data.get('gtdLines')
            if gtd_lines == None:
                print(" "*4, "Empty GTD lines!")
                break
            for gtd_line in gtd_lines:
                find_article('EB0003/A3L70/NS')
                #incomplete_plu()
                #print(json.dumps(gtd_line, ensure_ascii=False, indent=2)) 
                #break       
            if log_files:
                with open(r"D:\TEMP\GtdLines_" + str(page)+ ".json", 'w') as f:
                    json.dump(resp_json, f, ensure_ascii=False, indent=2)
                #break # For debugging: stop after the first page
        elif response.status_code == 204:
            print(" "*4, "Page is empty.")
            break
        else:
            print(" "*4, f"Error: {response.status_code}")
        page += 1
    print("Finished.")




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script































