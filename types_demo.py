'''
    Strings demo Glibs Python scripts
'''
#!/usr/bin/python3
import asyncio
import glibs_tools
import datetime
import sys
import time

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    #demo_types()
    demo_string()
    #demo_string_functions()
    #demo_string_formatting()
    #demo_dates()
    #test()

def demo_types():
    print("==== Demo of type conversion ====")
    x = 1
    y = "a"
    z = 1.11
    print(str(x) + " " + y)
    print(int(z))
    a = "123"
    b = 25
    print(int(a) + b)
    c = "1.11"
    print(float(c) + z)
    d = "4a5b6"
    #print(int(d)) # This will raise a ValueError because the string contains non-numeric characters
    print(d.isdigit()) # False, because the string contains non-numeric characters
    x = None # NULL type
    print(x) # None

def demo_string():
    print("==== Strings ====")
    s1 = "Test!"
    print(s1)
    s2 = 'Test!'
    print(s2)
    mls = ("123"
    "456") # Multiline string
    print(mls) # 123456
    mlt = '''Multiline text 1
Multiline text 2
Multiline text 3'''
    print(mlt)
    sa = "12345!"
    print(sa[1]) # 2
    print(sa[-2]) # 5
    print("0123456789"[2:4]) # Substring: 23 
    print("0123456789"[:3]) # Substring: 012
    print("0123456789"[7:]) # Substring: 789
    print("0" * 5 + "1") # 000001
    path = r"C:\python\name.txt"
    print(path)

def demo_string_functions():
    print("==== String functions ====")
    print("aBcD".lower()) # abcd
    print("aBcD".upper()) # ABCD
    print(ord(" ")) # 32
    print(chr(9)) # \t
    print(len("012345")) # 6
    print("12" in "012345667") # True
    print("ab" not in "012345667") # True
    print("  ab  ".strip()) # ab
    print("0123456789".find("23")) # 2
    print((" 0123456789 " * 5).replace("45", "abcd")) #  0123abcd6789  0123abcd6789  0123abcd6789  0123abcd6789  0123abcd6789 
    print((" 0123456789 " * 5).replace("45", "abcd", 3)) #  0123abcd6789  0123abcd6789  0123abcd6789  0123456789  0123456789 
    print(("123;456;789").split(";")) # ['123', '456', '789']
    print("; ".join(["123","456","789"])) # From list: 123; 456; 789 
    print("; ".join(("123","456","789"))) # From tuple: 123; 456; 789
    print(" ".join("0123456789")) # From sring array: 0 1 2 3 4 5 6 7 8 9
    print("12345".isnumeric()) # True
    print("1a2b3".isnumeric()) # False

def demo_string_formatting():
    print("==== String formatting ====")
    print("P1: {}. P2: {}.".format("1", "2")) # P1: 1. P2: 2.
    print("P1: {0}. P2: {1}.".format("1", "2")) # P1: 1. P2: 2.
    #print("P1: {1}. P2: {2}.".format("1", "2")) # Out of array range exception! Parameter 0 & 1 exists, parameter 2 does not exist.
    print("P1: {0}. P2: {0}.".format("1", "2")) # P1: 1. P2: 1.

def demo_dates():
    print("==== Demo of dates ====")
    dd = datetime.date.today()
    print(dd)
    dt = datetime.datetime.today()
    print(dt)
    time.sleep(0.5) # Seconds
    dt_2 = datetime.datetime.today()
    print(dt_2 - dt)
    async def xSleep(s):
        await asyncio.sleep(s) # Seconds
    asyncio.run(xSleep(0.3))
    dt_3 = datetime.datetime.today()
    print(dt_3 - dt_2)
    dt_4 = datetime.datetime.strptime("01-01-2027 00:00:00", "%d-%m-%Y %H:%M:%S")
    print(dt_4)
    dt_5 = datetime.datetime.strptime("01-01-27 00:00:00", "%d-%m-%y %H:%M:%S")
    print(dt_5)




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








