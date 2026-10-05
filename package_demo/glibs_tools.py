'''
    Glibs Python scripts tools
'''
#!/usr/bin/python3
import os
import subprocess
import sys

def main(_args):
    menu()

def menu():
    clear_console()    
    test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        



def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








