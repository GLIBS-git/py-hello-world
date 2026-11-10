'''
    Collections demo Glibs Python scripts
'''
#!/usr/bin/python3
import package_demo.glibs_base_tools as glibs_base_tools
import os
import sys

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    #demo_module()
    #demo_module_methods()
    demo_os()
    #test()

def demo_module():
    print("==== Module path ====")
    # The sys.path list contains the directories that Python searches for modules when you use an import statement. The order of the directories in this list determines the order in which Python searches for modules.
    print(sys.path) # ['/home/glibs/GitHub/py-hello-world', '/usr/lib/python314.zip', '/usr/lib/python3.14', '/usr/lib/python3.14/lib-dynload', '/home/glibs/GitHub/py-hello-world/.venv/lib/python3.14/site-packages']
    # Gets the value of the PYTHONPATH environment variable
    print(os.getenv("PYTHONPATH")) # None
    #sys.path.append('/path/to/module/collection') # Adds a new path to the module search path
    #import my_module # Imports a module from the specified path
    #export PYTHONPATH="/path/to/module/collection:$PYTHONPATH" # Adds a new path to the module search path in Linux or macOS (bash shell)

def demo_module_methods():
    print("==== Demo of system names ====")
    print(__name__) # Prints the name of the current module
    print(__file__) # Prints the path of the current module
    #print(__package__) # Prints the package of the current module
    print(sys.platform) # Prints the platform (e.g., win32, linux, darwin)
    print(sys.version) # Prints the Python version

def demo_os():
    print("==== Demo of os module ====")
    print(os.getcwd()) # Prints the current working directory






def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








