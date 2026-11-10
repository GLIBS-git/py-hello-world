'''
    Mathematics demo Glibs Python scripts
'''
#!/usr/bin/python3
from decimal import Decimal, ROUND_HALF_UP
import package_demo.glibs_base_tools as glibs_base_tools
import random
import sys

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    #demo_arythmetic()
    #demo_decimal()
    #demo_random()
    demo_bitwise()
    #test()

def demo_arythmetic():
    print("==== Demo of arythmetic ====")
    a = 7
    b = 2
    print(a + b)
    print(a / b)
    print(a // b) # 3
    print(a % b) # 2
    print(a ** b) # a^b
    print(round(1/3, 4))
    i = 0
    i += 1
    print(i)
    print()
    print(pow(2, 3))
    print(abs(-1))
    print(min(1, 2, 3))
    print(max(1, 2, 3))

def demo_decimal():
    print("==== Demo of decimal type ====")
    dn1 = Decimal("1.11111")
    dn2 = Decimal("1.11111")
    print(dn1 + dn2)
    dn3 = dn1 + dn2
    print(dn3)
    dn4 = dn1 * dn2
    print(dn4)
    dn5 = dn4.quantize(Decimal("1.00")) # dn4 is untouched
    print(dn4)
    print(dn5)
    print()
    print(Decimal("1.45").quantize(Decimal("1.0"))) # Not standard mathematical rounding
    print(Decimal("1.35").quantize(Decimal("1.0"))) # Not standard mathematical rounding
    print(Decimal("1.25").quantize(Decimal("1.0"))) # Not standard mathematical rounding
    print(Decimal("1.15").quantize(Decimal("1.0"))) # Not standard mathematical rounding
    print()
    print(Decimal("1.45").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print(Decimal("1.35").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print(Decimal("1.25").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print(Decimal("1.15").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print(Decimal("1.14").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print()
    print(Decimal("9").sqrt())
    print(Decimal("3").sqrt())
    print(Decimal("2")**2)
    print(Decimal("1.1")**2)
    print(pow(Decimal("1.1"),2))

def demo_random():
    print("==== Demo random numbers ====")
    print(random.random()) # 0 <= Random float number < 1
    print(random.random() * 100) # 0 <= Random float nunber < 100
    print(random.randint(1, 100)) # 1 <= Random integer number < 100
    print(random.randint(-100, 100)) # -100 <= Random integer number < 100
    print(random.randrange(-100, 100)) # -100 <= Random integer number < 100
    print(random.randrange(-100, 100, 5)) # -100 <= Random integer number step 5 < 100
    num_list = list()
    for i in range(10):
        num_list.append(i)
    print(num_list)
    print(random.choice(num_list)) # Select any element from the list
    print(random.choice(num_list))
    random.shuffle(num_list) # Shuffle the list
    print(num_list) # Shffled list
    char_list = []
    for c in "abcdefghijklmno".upper():
        char_list.append(c)
    print(char_list)
    print(random.choice(char_list)) # Select any element from the list
    print(random.choice(char_list))

def demo_bitwise():
    print("==== Demo bitwise operations ====")
    a: int = 5  # 101 in binary
    b: int = 3  # 011 in binary
    print(a & b)  # 001 (1 in decimal)
    print(a | b)  # 111 (7 in decimal)
    print(a ^ b)  # 110 (6 in decimal)
    print(~a)  # -6 (complement of a)
    print(a << 1)  # 1010 (10 in decimal)
    print(a >> 1)  # 010 (2 in decimal)
    print(int(0b1000)) # 8
    byte: bytes = bytes([8])
    print(byte) # b'\x08'
    print(f'{byte[0]:b}') # 1000
    print(f'{byte[0]:08b}') # 00001000
    print(byte[0] & 1) # 0
    print(byte[0] >> 1 & 1) # 0
    print(byte[0] >> 2 & 1) # 0
    print(byte[0] >> 3 & 1) # 1



def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








