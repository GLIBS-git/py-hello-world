'''
    Enum demo Glibs Python scripts
'''
#!/usr/bin/python3
from enum import Enum, auto
import package_demo.glibs_base_tools as glibs_base_tools
import sys

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    # Uncomment the test you want to run:
    use_enum()
    #test()


class Colors(Enum):
    TRANSPARENT = 0
    WHITE = 1
    BLACK = 2


class ColorShorts(Enum):
    TRANSPARENT = "TR"
    WHITE = "WH"
    BLACK = "BL"


class Nums(Enum):
    ONE = auto() # auto() automatically assigns numbers starting from 1
    TWO = auto()
    THREE = auto()


def use_enum():
    print("==== Using enums ====")
    print(Colors.WHITE) # Colors.WHITE
    print(Colors.WHITE.name) # WHITE
    print(Colors.WHITE.value) # 1
    print(ColorShorts.WHITE) # ColorShorts.WHITE
    print(ColorShorts.WHITE.name) # WHITE
    print(ColorShorts.WHITE.value) # WH
    print(Nums.ONE.value) # 1
    print(Nums.TWO.value) # 2
    print(Nums.THREE.value) # 3
    #print(Nums(5)) # ValueError exception
    print(Nums(2)) # Nums.TWO
    print(Nums(2).name) # TWO
    print(Nums(2).value) # 2
    print(len(Nums)) # 3
    print(list(Nums)) # [<Nums.ONE: 1>, <Nums.TWO: 2>, <Nums.THREE: 3>]


def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








