# Rename to secrets_demo.py and fill in your own values for app_key and client_id
# Real secrets are not pushed to GitHub for security reasons. You can use the template below to create your own web_request_secrets.py file.

def data_ref_url():
    return "https://server.com:1234/api/v1"

def app_key_1s(legal_entity):
    if legal_entity == "ABC":
        return 'app-key'
    else: 
        raise ValueError(f"Unknown legal entity: {legal_entity}!")

def client_id_1s(legal_entity):
    if legal_entity == "ABC":
        return 'client-id'   
    else: 
        raise ValueError(f"Unknown legal entity: {legal_entity}!")

def stock_service_sql_connection_string():
    return (
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=ServerName;'
        'Database=DbName;'
        'Trusted_Connection=yes;'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
        'Application Name=Glibs Python demo scripts;'
        'MultiSubnetFailover=yes'
    )









