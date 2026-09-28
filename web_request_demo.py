import requests

base_url = 'https://axweb-vdi:8454/Fashion.DataRef.svc/gtdLines'
headers = {
    'AppKey': 'your_app_key_here',
    'ClientId': 'your_client_id_here'
}
query_options = {
    'journalId': 'Гтд0017612',
    'page': '1'
}
response = requests.get(base_url, params=query_options, headers=headers, verify=False)  # Set verify=False to ignore SSL certificate warnings
if response.status_code == 200:
    print("Success!")
    print(response.json())  # Print the JSON response
else:
    print(f"Error: {response.status_code}")
















