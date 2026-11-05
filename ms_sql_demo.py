'''
    MS SQL demo Glibs Python scripts
'''
#!/usr/bin/python3
import datetime
import package_demo.glibs_tools as glibs_tools
import package_demo.secrets_demo as secrets
import pyodbc
import sys

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    #read_ms_sql()
    #read_ms_sql_2()
    read_ms_sql_3()
    #test()

def read_ms_sql():
    print("==== Reading MS SQL one record ====")
    with pyodbc.connect(secrets.stock_service_sql_connection_string()) as conn:
        query = "SELECT TOP 1 [ItemId], [Name] FROM [Items] WHERE [ItemId] = ?;"
        cursor = conn.cursor()
        cursor.execute(query, ('7124813',))
        for row in cursor:
            print(row) # ('7124813', 'Футболка')
            print(row.ItemId, row.Name) # 7124813 Футболка
            print(row[0], row[1]) # 7124813 Футболка

def read_ms_sql_2():
    print("==== Reading MS SQL batch records ====")
    start = datetime.datetime.now()
    with pyodbc.connect(secrets.stock_service_sql_connection_string()) as conn:
        query = "SELECT TOP 10000 [ItemId], [Name] FROM [Items] WHERE [ItemId] LIKE ?;"
        cursor = conn.cursor()
        crit = '7%'
        #cursor.execute(query, ('7%',))
        cursor.execute(query, (crit,))
        i = 0
        for row in cursor:
            i +=1
            print(f"{i}: {row}")
    print(f"Time taken: {datetime.datetime.now() - start}")

def read_ms_sql_3():
    print("==== Reading MS SQL batch records ====")
    start = datetime.datetime.now()
    with pyodbc.connect(secrets.test_db_sql_connection_string()) as conn:
        query = "SELECT * FROM [Product];"
        cursor = conn.cursor()
        cursor.execute(query)
        i = 0
        for row in cursor:
            i +=1
            print(f"{i}: {row}")
    print(f"Time taken: {datetime.datetime.now() - start}")



def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








