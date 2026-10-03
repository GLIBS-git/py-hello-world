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
        f1.write("Test content!") # Adds one more piece of text
        f1.write("Test content!") # Adds one more piece of text
    if os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r") as f1:
            print(f1.read()) # Test content!Test content!Test content!
    print()
    with open(TMP_FILE_PATH, "w") as f1:
        f1.write("Test content!\n")
        f1.write("Test content!\n")
        f1.write("Test content!\n")
    if os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r") as f1:
            print(f1.read()) # Three lines with line breaks
    print()
    txt_l = []
    #for i in range (1, 8):
    #    txt_l.append(f"Test content {i}!")
    txt_l = [f"Test content {i}!" for i in range(1, 8)]
    with open(TMP_FILE_PATH, "w") as f1:
        f1.writelines(txt_l)
    if os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r") as f1:
            print(f1.read())
    print()
    txt = str.join("\n", txt_l)
    with open(TMP_FILE_PATH, "w") as f1:
        f1.write(txt)
    if os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r") as f1:
            print(f1.read())
    print()

def demo_files_2():
    print("==== File create, read, part 2 ====")
    TMP_FILE_PATH = r'/home/glibs/Tmp/Py_test.txt'
    if os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r") as f1:
            for l in f1:
                print(l)
            f1.seek(0)
            print(f1.read())
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








