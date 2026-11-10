'''
    Console demo Glibs Python scripts
'''
#!/usr/bin/python3
import package_demo.glibs_base_tools as glibs_base_tools
import sys

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    #demo_print()
    #demo_input()
    demo_print_streams()
    #test()

def demo_print():
    print("==== Demo of 'print' ====")
    print("Hello world!") # Hello world!
    print(2 * 2) # 4
    print(f"2 * 2 = {2 * 2}") # 2 * 2 = 4
    print("123", "789", sep=" ", end=" "); print("456") # 123 789 456
    path = r"D:\Python\Source" # D:\Python\Source, but D:\Python\Source\ not working, because the last backslash is an escape character, so it needs to be escaped with another backslash or use raw string.
    print(path) # D:\Python\Source
    print(1); print(2); print(3) # This way is possible: 1\n2\n3
    print("Value 1: {}.    Value 2: {}.    Value 3: {}.".format(1, 2, 3)) # Formatting a string: Value 1: 1.    Value 2: 2.    Value 3: 3.
    print ("Text 1 " \
        "Text 2") # Printing multiline text. No spaces after "\"! : Text 1 Text 2

def demo_input():
    print("==== Demo of console input ====")
    inp = input("Enter text: ")
    print()
    print(f"You entered: {inp}")

def demo_print_streams():
    print("==== Demo of print streams ====")
    print("This goes to stdout")
    print("This goes to stderr", file=sys.stderr)





def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








