'''
    MS SQL demo Glibs Python scripts
'''
#!/usr/bin/python3
import package_demo.glibs_tools as glibs_tools
import package_demo.secrets_demo as secrets
import pyodbc
import sys

def main(_args):
    read_ms_sql()
    menu()

def menu():
    glibs_tools.clear_console()    
    read_ms_sql()
    #test()

def read_ms_sql():
    print("==== Reading MS SQL ====")
    with pyodbc.connect(secrets.stock_service_sql_connection_string()) as conn:
        query = "SELECT TOP 1 [ItemId], [Name] FROM [Items] WHERE [ItemId] = ?;"
        cursor = conn.cursor()
        cursor.execute(query, ('7124813',))
        for row in cursor:
            print(row)
            print(row.ItemId, row.Name)


def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








