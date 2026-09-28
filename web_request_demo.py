import requests
import json
import web_request_secrets as secrets

base_url = 'https://axweb-vdi:8454/Fashion.DataRef.svc/gtdLines'
headers = {}
headers['AppKey'] = secrets.app_key()
headers['ClientId'] = secrets.client_id()
query_options = {}
query_options['journalId'] = 'Гтд0017612'
continue_read = True
page = 1
while continue_read:
    query_options['page'] = str(page)
    print("Reading page: ", page)
    response = dict(requests.get(base_url, params=query_options, headers=headers, verify=False))  # Set verify=False to ignore SSL certificate warnings
    if response.status_code == 200:
        if response == None:
            print(" "*4, "Empty response!")
            break
        print(" "*4, "Lines on page: ", response.get('data', '0'))
        data = response.get('data')
        if data == None:
            print(" "*4, "Data is empty!")
            break
        gtd_lines = data.get('gtdLines')
        if gtd_lines == None:
            print(" "*4, "Empty GTD lines!")
            break
        for gtd_line in gtd_lines:
            print(json.dumps(gtd_line, indent=2)) 
            break       
        with open(r"D:\TEMP\GtdLines_" + str(page)+ ".txt", 'w') as f:
            json.dump(response.json(), f, indent=2)
    elif response.status_code == 204:
        print(" "*4, "Page is empty.")
        continue_read = False
    else:
        print(" "*4, f"Error: {response.status_code}")
print("Finished.")
















