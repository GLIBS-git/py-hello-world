'''
    Strings demo Glibs Python scripts
'''
#!/usr/bin/python3
import asyncio
import package_demo.glibs_base_tools as glibs_base_tools
import datetime
import sys
import time

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    #demo_types()
    #demo_string()
    #demo_string_functions()
    #string_formatting()
    string_prefixes()
    #demo_dates()
    #demo_binary()
    #test()

def demo_types():
    print("==== Demo of type conversion ====")
    x = 1
    y = "a"
    z = 1.11
    print(str(x) + " " + y) # 1 a
    print(int(z)) # 1
    a = "123"
    b = 25
    print(int(a) + b) # 148
    c = "1.11"
    print(float(c) + z) # 2.22
    d = "4a5b6"
    #print(int(d)) # This will raise a ValueError because the string contains non-numeric characters
    print(d.isdigit()) # False, because the string contains non-numeric characters
    e = "123456"
    print(e.isdigit()) # True, because the string contains only numeric characters
    print(e.isnumeric()) # True, because the string contains only numeric characters
    print(e.isdecimal()) # True, because the string contains only decimal characters
    # ! ! ! .isdigit() returns True only if the string contains only digits and is not empty. It does not consider decimal points, negative signs, or any other characters as digits.
    e = "123.456"
    print(e.isdigit()) # False, because the string contains a decimal point 
    print(e.isnumeric()) # False, because the string contains a decimal point
    print(e.isdecimal()) # False, because the string contains a decimal point
    e = "-123456"
    print(e.isdigit()) # False, because the string contains a negative sign
    print(e.isnumeric()) # False, because the string contains a negative sign
    print(e.isdecimal()) # False, because the string contains a negative sign
    e = "1/2"
    print(e.isdigit()) # False, because the string contains a fraction
    print(e.isnumeric()) # False, because the string contains a fraction
    print(e.isdecimal()) # False, because the string contains a fraction
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

def string_formatting():
    print("==== String formatting ====")
    print("P1: {}. P2: {}.".format("1", "2")) # P1: 1. P2: 2.
    print("P1: {0}. P2: {1}.".format("1", "2")) # P1: 1. P2: 2.
    #print("P1: {1}. P2: {2}.".format("1", "2")) # Out of array range exception! Parameter 0 & 1 exists, parameter 2 does not exist.
    print("P1: {0}. P2: {0}.".format("1", "2")) # P1: 1. P2: 1.

def string_prefixes():
    print("==== String prefixes ====")
    print("Raw string: C:\python\name.txt") # Raw string: C:\python
                                            # ame.txt
    print(r"Raw string: C:\python\name.txt") # Raw string: C:\python\name.txt
    print(f"Formatted string: {1+1}") # Formatted string: 2
    b = b"Byte string: \x41\x42\x43" # Byte string: ABC
    print(b)
    print(type(b)) # <class 'bytes'>

def demo_dates():
    print("==== Demo of dates ====")
    # import datetime
    dd = datetime.date.today()
    print(dd) # 2026-11-12
    dt = datetime.datetime.today()
    print(dt) # 2026-11-12 10:30:45.123456
    time.sleep(0.5) # Seconds
    dt_2 = datetime.datetime.today()
    print(dt_2 - dt) # 0:00:00.500000
    # import asyncio
    async def xSleep(s):
        await asyncio.sleep(s) # Seconds
    asyncio.run(xSleep(0.3))
    asyncio.run(asyncio.sleep(0.3))
    dt_3 = datetime.datetime.today()
    print(dt_3 - dt_2) # 0:00:00.300000
    dt_4 = datetime.datetime.strptime("01-01-2027 00:00:00", "%d-%m-%Y %H:%M:%S")
    print(dt_4) # 2027-01-01 00:00:00
    dt_5 = datetime.datetime.strptime("01-01-27 00:00:00", "%d-%m-%y %H:%M:%S")
    print(dt_5) # 2027-01-01 00:00:00

def demo_binary():
    print("==== Demo of binary data ====")
    byte: int = 0b10101010 # Set binary value
    print(byte) # 170
    byte2 = 0xFF # Set hexadecimal value
    print(byte2) # 255
    byte3 = 0o77 # Set octal value
    print(byte3) # 63
    byte4 = bytes([0b10101010, 0xFF, 0o77]) # Create bytes object
    print(byte4) # b'\xaa\xff?'
    print(type(byte4)) # <class 'bytes'>
    print(byte4[0]) # 170
    print(byte4[1]) # 255
    print(byte4[2]) # 63
    array = bytearray([0b10101010, 0xFF, 0o77]) # Create bytearray object
    print(array) # bytearray(b'\xaa\xff?')
    print(type(array)) # <class 'bytearray'>
    print(array[0]) # 170
    print(array[1]) # 255
    print(array[2]) # 63
    ba = bytearray()
    print(ba) # bytearray(b'')
    ba[0] = 0b10101010 # Set value at index 0
    ba[1] = 0xFF # Set value at index 1
    print(ba) # bytearray(b'\xaa\xff')




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








