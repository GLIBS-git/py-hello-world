'''
    Files demo Glibs Python scripts
'''
#!/usr/bin/python3
import glibs_tools
import os
import sys

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    demo_files()
    #test()

def demo_files():
    print("==== File create, read ====")
    TMP_FILE_PATH = r'/home/glibs/Tmp/Py_test.txt'
    with open(TMP_FILE_PATH, "w") as f1:
        f1.write("Test content!")
    if os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r") as f1:
            for l in f1:
                print(l)
        with open(TMP_FILE_PATH, "r") as f1:
            print(f1.read())
    with open(TMP_FILE_PATH, "a") as f1:
        f1.write("Test content 2!")
        f1.write("Test content 3!")
    if os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r") as f1:
            for l in f1:
                print(l)
        with open(TMP_FILE_PATH, "r") as f1:
            print(f1.read())




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








