'''
    JSON demo Glibs Python scripts
'''
#!/usr/bin/python3
import json
import os
import subprocess
import sys

def main(_args):
    menu()

def menu():
    clear_console()    
    #demo_json_encode_decode()
    demo_json_encode_complex()
    #test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
def demo_json_encode_decode():
    print("==== JSON encode & decode ====")
    js = {"name": "John", "age": 30, "city": "New York"}
    print(type(js))
    print(js) 
    js_str = json.dumps(js, ensure_ascii=False, indent = 2) # Indent -- human readable format. Default ensure_ascii=True escapas all UNICODE symbols.
    print(js_str)
    js_2 = json.loads(js_str)
    print(type(js_2))
    print(js_2)
    print(js_2["name"]) # "John"
    print(js_2.get("name")) # "John"
    #print(js_2["Name"]) # This will raise a KeyError because "Name" is not a key in the dictionary. The correct key is "name".
    print(js_2.get("Name")) # This will return None because "Name" is not a key in the dictionary. The correct key is "name".
    print(js_2.get("Name", "Key not found")) # This will return "Key not found" because "Name" is not a key in the dictionary. The correct key is "name".
    if "Name" in js_2:
        print(js_2["Name"])
    else:
        print("Key not found") # This will print "Key not found" because "Name" is not a key in the dictionary. The correct key is "name".

def demo_json_encode_complex():
    print("==== Complex JSON encode ====")
    js = {
        "name": "John",
        "surname": "Smith",
        "age": 33,
        "city": "Los Angeles",
        "country": "USA",
        "languages": [
            {"name": "English", "level": "native"},
            {"name": "Spanish", "level": "intermediate"},   
            {"name": "French", "level": "beginner"}
        ],
        "isMarried": False,
        "children": ["Anna", "Bob"],
        "phone": ("Xiaomi", "Samsung"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1},
        ],
    }    
    print(type(js))
    print(js) 
    js_str = json.dumps(js, ensure_ascii=False, indent = 2) # Indent -- human readable format
    print(js_str)






def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








