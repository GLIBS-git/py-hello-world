'''
    Glibs learning Python test scripts
'''
#!/usr/bin/python3
import collections_demo
import console_demo
import json_demo
import logic_demo
#import math_demo as md # May be aliased
import math_demo
import os
import sys
import subprocess
import types_demo

def main(_args):
    menu()

def menu():
    clear_console()    
    # Uncomment the test you want to run:
    collections_demo.menu()
    #console_demo.menu()
    #logic_demo.menu()
    #math_demo.menu()
    #json_demo.menu()
    #types_demo.menu()
    #demo_exceptions()
    #demo_variables_and_inner_functions()
    #print(demo_function_return(1)) # The returned value can be of any type, int, str, list, dict, etc.
    #print(demo_function_return(2)) # The returned value can be of any type, int, str, list, dict, etc.
    #print(demo_a_la_ax_strfmt("Test: %1, %2!", "Text", 123)) # Dynamic parameters
    #print(demo_a_la_ax_strfmt(123, "Text", 123)) # Raises error
    #test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
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

def demo_variables_and_inner_functions():
    print("==== Local and global variables & inner functions ====")
    s = "Hello world!"
    print("Top function before: ", s)
    def inner_1():
        s = 0
        print("Local inner 1: ", s)
    inner_1()
    print("Top function after inner 1:", s)
    def inner_2():
        global t # Refers to variable defined outside all functions (only in main script)
        nonlocal s # Refers nearest variable from parent functions
        s = 0
        print("Local inner 2: ", s)
    inner_2()
    print("Top function after inner 2:", s)
    def printer(pt):
        print(pt)
    #printer("Hello world!", 1) # This will raise an error because the printer function is defined to take only one argument, but two arguments are provided. The second argument (1) is not expected by the function definition.


def demo_function_return(_case=1):
    print("==== Demo switch case ====")
    print(f"Parameter: {_case}")
    match _case:
        case 1:
            return 1
        case 2:
            return "Two"
        case _:
            return "Default case"

def demo_a_la_ax_strfmt(_template: str, *_values):
    print("==== Demo a-la Ax strfmt() ====")
    print("Parameters:")
    print(f"        Template: {_template}")
    print(f"        Values: {_values}")
    if not isinstance(_template, str):
        raise TypeError("The template parameter must be a string!")
    i = 0
    ret: str = _template
    for val in _values:
        i += 1
        ret = ret.replace(f"%{i}", str(val))
    return ret

def demo_async_io(): # Take info from Claude
    print("==== Demo async/await ====")

def demo_threading(): # Take info from Claude
    print("==== Demo async/await ====")



def test():
    print("==== Test ====")

if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








