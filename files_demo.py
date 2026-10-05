'''
    Files demo Glibs Python scripts
'''
#!/usr/bin/python3
from ast import If

import package_demo.glibs_tools as glibs_tools
import os
import sys

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    #demo_files()
    demo_files_2()
    #test()

def demo_files():
    print("==== File create, read ====")
    TMP_FILE_PATH = r'/home/glibs/Tmp'
    TMP_FILE_NAME = 'Py_test.txt'
    if not os.path.exists(TMP_FILE_PATH):
        os.makedirs(TMP_FILE_PATH) # Creates the directory if it does not exist
    TMP_FILE_FULL_PATH = os.path.join(TMP_FILE_PATH, TMP_FILE_NAME)
    print()
    print("="*10, "1", "="*10)
    with open(TMP_FILE_FULL_PATH, "w") as f1: # If directory does not exist, it will raise an error. If file does not exist, it will create a new file. 
                                         # If file exists, it will overwrite the content.
        f1.write("Test content!")
        f1.write("Test content!") # Adds one more piece of text
        f1.write("Test content!") # Adds one more piece of text
    if os.path.exists(TMP_FILE_FULL_PATH):
        with open(TMP_FILE_FULL_PATH, "r") as f1:
            print(f1.read())    # Test content!Test content!Test content!
                                # No line breaks.
    print()
    print("="*10, "2", "="*10)
    with open(TMP_FILE_FULL_PATH, "w") as f1:
        f1.write("Test content!\n")
        f1.write("Test content!\n")
        f1.write("Test content!\n")
    if os.path.exists(TMP_FILE_FULL_PATH):
        with open(TMP_FILE_FULL_PATH, "r") as f1:
            print(f1.read()) # Three lines with line breaks
    print()
    print("="*10, "3", "="*10)
    txt_l = []
    #for i in range (1, 8):
    #    txt_l.append(f"Test content {i}!")
    txt_l = [f"Test content {i}!" for i in range(1, 8)]
    with open(TMP_FILE_FULL_PATH, "w") as f1:
        f1.writelines(txt_l) # Does not add line breaks, so all content will be in one line
    if os.path.exists(TMP_FILE_FULL_PATH):
        with open(TMP_FILE_FULL_PATH, "r") as f1:
            print(f1.read()) # Test content 1!Test content 2!Test content 3!Test content 4!Test content 5!Test content 6!Test content 7!
    print()
    print("="*10, "4", "="*10)
    txt = str.join("\n", txt_l)
    with open(TMP_FILE_FULL_PATH, "w") as f1:
        f1.write(txt)
    if os.path.exists(TMP_FILE_FULL_PATH):
        with open(TMP_FILE_FULL_PATH, "r") as f1:
            print(f1.read()) # Output will be in multiple lines with line breaks

def demo_files_2():
    print("==== File create, read, part 2 ====")
    TMP_FILE_PATH = r'/home/glibs/Tmp'
    if not os.path.exists(TMP_FILE_PATH):
        raise Exception(f"Directory {TMP_FILE_PATH} does not exist. Please create it first.")
    TMP_FILE_NAME = 'Py_test.txt'
    if not os.path.exists(TMP_FILE_PATH):
        os.makedirs(TMP_FILE_PATH) # Creates the directory if it does not exist
    TMP_FILE_FULL_PATH = os.path.join(TMP_FILE_PATH, TMP_FILE_NAME)
    folder, file_name = os.path.split(TMP_FILE_FULL_PATH)
    print(f"Folder: {folder}")
    print(f"File name: {file_name}")
    txt_l = [f"Test content {i}!" for i in range(1, 8)]
    txt = str.join("\n", txt_l)
    print()
    with open(TMP_FILE_FULL_PATH, "w") as f1:
        f1.write(txt)
    if os.path.exists(TMP_FILE_FULL_PATH):
        with open(TMP_FILE_FULL_PATH, "r") as f1:
            print("="*10, "1", "="*10)
            for l in f1:
                print(l)
            print()
            print("="*10, "2", "="*10)
            f1.seek(0) # Read from the beginning of the file
            print(f1.read())
            print()
            print("="*10, "3", "="*10)
            f1.seek(0) # Read from the beginning of the file
            for l in f1:
                print(l.replace("\n", "")) # Remove line breaks when printing
    return
    print()
    print("="*10, "2", "="*10)
    with open(TMP_FILE_FULL_PATH, "a") as f1:
        f1.write("Test content 2!")
        f1.write("Test content 3!")
    if os.path.exists(TMP_FILE_FULL_PATH):
        with open(TMP_FILE_FULL_PATH, "r") as f1:
            print(f1.read())




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








