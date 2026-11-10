'''
    Exceptions demo Glibs Python scripts
'''
#!/usr/bin/python3
import collections_demo
import package_demo.glibs_base_tools as glibs_base_tools
import sys

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    demo_exceptions()
    #test()

def demo_exceptions():
    print("==== Demo of exceptions ====")
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("This block is executed regardless of whether an exception occurred or not.")
    print()
    try:
        raise ValueError("This is a custom error message.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    #except ValueError as ve:
    #    print(f"Error: Incorrect value: {ve}")
    #except (TypeError, NameError) as ve: # Several exceptions can be caught in one block
    #    print(f"Error: Incorrect value: {ve}")
    except RuntimeError as e:
        print(f"Runtime error caught: {e}")
    except Exception as e:
        print(f"General exception caught: {e}")
    finally:
        print("This block is executed regardless of whether an exception occurred or not.")




def test():
    print("==== Test ====")

if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








