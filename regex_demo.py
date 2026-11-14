'''
    Regular Expressions demo Glibs Python scripts
'''
#!/usr/bin/python3
import package_demo.glibs_base_tools as glibs_base_tools
import sys
import re

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    intro()
    #isPhone('')
    #test()

def intro():
    print("==== Intro ====")
    print(re.match('123', '123'))
    print(re.match('^123$', '123'))
    print(re.match('2', '123'))
    #
    print(re.findall('a', '123'))
    print(re.findall('2', '123'))
    print(re.findall('2', '123123123'))
    #
    print(re.fullmatch('123', '123'))
    print(re.fullmatch('^123$', '123'))
    print(re.fullmatch('2', '123'))
    #
    print(re.search('123', '123'))
    print(re.search('^123$', '123'))
    print(re.search('2', '123'))

    

def isPhone(phoneNumber: str):
    print("==== Check phone number ====")
    phoneNumList = [
        '123-45-67',
        '1234567',
        '123 45 67',
        '123456789',
        '12a456789',
    ]
    pattern = re.compile(r'\d{3}[\s-]?\d{2}[\s-]?\d{2}')
    for phoneNum in phoneNumList:
        #res = re.fullmatch(r'\d{3}[\s-]?\d{2}[\s-]?\d{2}', phoneNum)
        res = pattern.match(phoneNum)
        print(f"{phoneNum} -- {bool(res)}")


def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script














