'''
    Web server demo Glibs Python scripts
'''
#!/usr/bin/python3
import package_demo.glibs_tools as glibs_tools
import sys

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    simpleWebServer()
    #test()

def simpleWebServer():
    print("==== Simple Web Server ====")




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








