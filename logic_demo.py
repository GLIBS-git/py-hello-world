'''
    Logic operators demo Glibs Python scripts
'''
#!/usr/bin/python3
import sys
import os
import subprocess

def main(_args):
    menu()

def menu():
    clear_console()    
    #demo_logic_operators()
    #demo_logic_if()
    demo_logic_if_ternary()
    #demo_logic_if_dynamic_param(1) # Dynamic parameter for IF
    #demo_logic_if_dynamic_param("a") # Dynamic parameter for IF
    #demo_logic_switch_case_sycle(4)
    #demo_logic_switch_case_sycle(_case = 4) # The named parameters with different types, int or str, are supported in Python 3.10 and later.
    #demo_logic_switch_case_sycle(_case = "d") # The named parameters with different types, int or str, are supported in Python 3.10 and later.
    #test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
def demo_logic_operators():
    print("==== Demo of logic operators ====")
    a = 1
    b = 2
    c = 3 
    if a > b and b <= c:
        print("A")
    if a != b or b == c:
        print("B")
    if a != b or not(b == c):
        print("C")
    if "x" in "abcxyz":
        print("D")
    if "X" in "abcxyz":
        print("E")

def demo_logic_if():
    print("==== Demo of logic if ====")
    inp = input("Enter value: ")
    if inp.strip().lower() == "a":
        print("A!")
    elif inp.strip().lower() == "b":
        print("B!")
    elif inp.strip().lower() == "c":
        print("C!")
    else:
        print("Something else.")

def demo_logic_if_ternary(): # Ternary operator
    print("==== Demo of ternary operator ====")
    a = 1
    b = 2
    print("A") if a > b else print("B")

def demo_logic_if_dynamic_param(_cond):
    print("==== Demo of logic if dynamic parameter type ====")
    print(f"Parameter: {_cond}")
    if _cond == "a" or _cond == 1:
        print("A!")
    elif _cond == "b" or _cond == 2:
        print("B!")
    elif _cond == "c" or _cond == 3:
        print("C!")
    else:
        pass # Do nothing, just skip to the next statement

def demo_logic_switch_case_sycle(_case = 1): # Dynamic parameter type, can be int or str
    print("==== Demo switch case ====")
    print(f"Parameter: {_case}")
    match _case:
        case 1 | "a":
            for i in range(10):
                print(i) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        case 2 | "b":
            for i in range(5, 10):
                    print(i) #5, 6, 7, 8, 9
        case 3 | "c":
            for i in range(5, 10, 2):
                print(i) #5, 7, 9
        case 4 | "d":
            for ch in "Hello world!":
                print(ch) #H, e, l, l, o,  , w, o, r, l, d, !
        case _:
            print("Default case")




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








