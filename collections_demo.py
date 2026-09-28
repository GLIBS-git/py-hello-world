'''
    Collections demo Glibs Python scripts
'''
#!/usr/bin/python3
import sys
import os
import subprocess

def main(_args):
    menu()

def menu():
    clear_console()    
    #demo_lists()
    #demo_tuples()
    #demo_dictionaries()
    demo_dictionaries_2()
    #test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
def demo_lists():
    print("==== Lists ====")
    emptyList = []
    print(emptyList) # []
    emptyList_2 = list()
    print(emptyList_2) # []
    numList = [1, 2, 3, 4, 5]
    print(numList) # [1, 2, 3, 4, 5]
    print(numList[2]) # 3
    numList.append(6) # Add 6 to the end of the list
    print(numList) # [1, 2, 3, 4, 5, 6]
    numList.insert(0, 0) # Add 0 to the beginning of the list
    print(numList) # [0, 1, 2, 3, 4, 5, 6]
    charList = ["A", "B", "C", "D", "E"]
    print(charList) # ["A", "B", "C", "D", "E"]
    print(charList[2]) # "C"
    print(charList.index("C")) # 2
    print(charList[:2]) # ["A", "B"]
    print(charList[2:4]) # ["C", "D"]
    print(charList[3:]) # ["D", "E"]
    #print(charList.index("c")) # ValueError: 'c' is not in list
    if "c" in charList:
        print(charList.index("c"))
    charList[2] = "c" # Change "C" to "c"
    print(charList) # ["A", "B", "c", "D", "E"]
    print(len(["A", "B", "C", "D", "E"])) # 5
    print(len("abcdef")) # 6
    print(min([1, 2, 3, 4, 5])) # 1
    print(max([1, 2, 3, 4, 5])) # 5
    print([1, 2, 3, "a", "b", "c"]) # [1, 2, 3, 'a', 'b', 'c']

def demo_tuples(): # Immutable lists
    print("==== Tuples ====")
    emptyTuple = ()
    print(emptyTuple) # ()
    emptyTuple_2 = tuple()
    print(emptyTuple_2) # ()
    numTuple = (1, 2, 3, 4, 5)
    print(numTuple) # (1, 2, 3, 4, 5)
    print(numTuple[2]) # 3
    #numTuple[2] = 3 # TypeError: 'tuple' object does not support item assignment (immutable)
    print(len((1, 2, 3, 4, 5))) # 5
    print(min((1, 2, 3, 4, 5))) # 1
    print(max((1, 2, 3, 4, 5))) # 5
    print((1, 2, 3, "a", "b", "c")) # (1, 2, 3, 'a', 'b', 'c')

def demo_dictionaries(): # Mutable key-value pairs
    print("==== Dictionaries ====")
    emptyDict = {}
    print(emptyDict) # {}
    emptyDict_2 = dict()
    print(emptyDict_2) # {}
    numDict = {"one": 1, "two": 2, "three": 3}
    print(numDict) # {'one': 1, 'two': 2, 'three': 3}
    print(numDict["two"]) # 2
    #print(numDict["seven"]) # Throws KeyError
    print(numDict.get("two")) # 2
    print(numDict.get("seven", "Value not found")) # Value not found
    print(numDict.get("seven")) # None
    if "Two" in numDict:
        print(numDict["Two"])
    else:
        print("Key not found") # This will print "Key not found" because "Two" is not a key in the dictionary. The correct key is "two".
    numDict["four"] = 4 # Add a new key-value pair
    print(numDict) # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    print(len({"one": 1, "two": 2, "three": 3})) # 3
    print(min({"one": 1, "two": 2, "three": 3})) # one
    print(max({"one": 1, "two": 2, "three": 3})) # two
    d_1 = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}
    print(d_1) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    d_2 = {1:"a", 1:"a"}
    print(d_2) # {1: 'a'}
    d_2 = {1:"a", 1:"b", 1:"c"}
    print(d_2) # {1: 'c'}

def demo_dictionaries_2(): # Mutable key-value pairs
    print("==== Dictionaries part 2 ====")
    l = [
        [1, "One"],
        [2, "Two"],
        [3, "Three"],
        [4, "Four"],
        [5, "Five"], # Comma is not an error
    ]
    print(l)
    d = dict(l)
    print(d)
    l2 = [
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Four"),
        (5, "Five"),
    ]
    print(l2)
    d2 = dict(l)
    print(d2)




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








