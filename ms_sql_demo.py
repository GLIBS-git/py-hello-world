'''
    MS SQL demo Glibs Python scripts
'''
#!/usr/bin/python3
import glibs_tools
import pyodbc
import sys

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    #test()

def read_ms_sql():
    print("==== Reading MS SQL ====")




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








