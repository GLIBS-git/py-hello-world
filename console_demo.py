'''
    Console demo Glibs Python scripts
'''
#!/usr/bin/python3
import sys
import os
import subprocess

def main(_args):
    menu()

def menu():
    clear_console()    
    demo_print()
    #demo_print_sys_names()
    #demo_input()
    #test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
def demo_print():
    print("==== Demo of 'print' ====")
    print("Hello world!")
    print(2 * 2)
    print(f"2 * 2 = {2 * 2}")
    print("123", "789", sep=" ", end=" ")
    print("456")
    path = r"D:\Python\Source" # D:\Python\Source, but D:\Python\Source\ not working, because the last backslash is an escape character, so it needs to be escaped with another backslash or use raw string.
    print(path)
    print(1); print(2); print(3) # This way is possible
    print("Value 1: {}.    Value 2: {}.    Value 3: {}.".format(1, 2, 3)) # Formatting a string
    print ("Text 1 " \
        "Text 2") # Printing multiline text. No spaces after "\"!

def demo_print_sys_names():
    print("==== Demo of system names ====")
    print(__name__) # Prints the name of the current module
    print(__file__) # Prints the path of the current module
    #print(__package__) # Prints the package of the current module
    print(sys.platform) # Prints the platform (e.g., win32, linux, darwin)
    print(sys.version) # Prints the Python version

def demo_input():
    print("==== Demo of console input ====")
    inp = input("Enter text: ")
    print()
    print(inp)




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








