'''
    Run another command or application demo Glibs Python scripts
'''
#!/usr/bin/python3
import os
import package_demo.glibs_base_tools as glibs_base_tools
import subprocess
import sys

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    subproc()
    #test()

def subproc():
    print("==== Run a subprocess ====")
    if os.name == "nt":
        result = subprocess.run(['cmd', "/c", 'dir'], capture_output=True, text=True) # Problem with encoding
        #result = subprocess.run(['cmd', "/c", 'chcp 65001 >nul && dir'], capture_output=True, encoding='utf-8', errors='replace') # Not working
        #result = subprocess.run(['cmd', "/c", 'dir'], capture_output=True, encoding=oem_cp, errors='replace') # Runtime exception
    else:
        result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
    print('stdout:')
    print(result.stdout)
    print('stderr:')
    print(result.stderr)
    print('returncode:')
    print(result.returncode)



def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








