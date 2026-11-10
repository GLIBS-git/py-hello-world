'''
    Threading & async/await demo Glibs Python scripts
'''
#!/usr/bin/python3
import package_demo.glibs_base_tools as glibs_base_tools
import sys

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    #test()

def demo_async_io(): # Take info from Claude
    print("==== Demo async/await ====")

def demo_threading(): # Take info from Claude
    print("==== Demo threading ====")



def test():
    print("==== Test ====")

if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








