import requests
import json
import web_request_secrets as secrets

base_url = 'https://axweb-vdi:8454/Fashion.DataRef.svc/gtdLines'
headers = {}
headers['AppKey'] = secrets.app_key()
headers['ClientId'] = secrets.client_id()
query_options = {}
query_options['journalId'] = 'Гтд0017612'
page = 1
while True:
    query_options['page'] = str(page)
    print("Reading page: ", page)
# Error here
    #response = dict(requests.get(base_url, params=query_options, headers=headers, verify=False))  # Set verify=False to ignore SSL certificate warnings
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
            print(json.dumps(gtd_line, indent=2)) 
            break       
        with open(r"D:\TEMP\GtdLines_" + str(page)+ ".json", 'w') as f:
            json.dump(resp_json, f, indent=2)
    elif response.status_code == 204:
        print(" "*4, "Page is empty.")
        break
    else:
        print(" "*4, f"Error: {response.status_code}")
    page += 1
print("Finished.")
















