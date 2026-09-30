'''
    Collections demo Glibs Python scripts
'''
#!/usr/bin/python3
import glibs_tools
import os
import sys

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    module_demo()
    #test()

def module_demo():
    print("==== Module path ====")
    print(sys.path)
    # PYTHONPATH environment variable
    print(os.getenv("PYTHONPATH")) # Gets the value of the PYTHONPATH environment variable
    #sys.path.append('/path/to/module/collection') # Adds a new path to the module search path
    #import my_module # Imports a module from the specified path
    #export PYTHONPATH="/path/to/module/collection:$PYTHONPATH" # Adds a new path to the module search path in Linux or macOS (bash shell)



def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








