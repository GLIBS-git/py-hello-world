'''
    JSON demo Glibs Python scripts
'''
#!/usr/bin/python3
import package_demo.glibs_base_tools as glibs_base_tools
import json
import sys

def main(_args):
    menu()

def menu():
    glibs_base_tools.clear_console()    
    #demo_json_encode_decode()
    #demo_json_encode_complex()
    demo_json_encode_text()
    #test()

def demo_json_encode_decode():
    print("==== JSON encode & decode ====")
    js = {"name": "John", "age": 30, "city": "New York"}
    print(type(js))
    print(js) 
    js_str = json.dumps(js, ensure_ascii=False, indent=2) # Indent -- human readable format. Default ensure_ascii=True escapas all UNICODE symbols.
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
    js_str = json.dumps(js, ensure_ascii=False, indent=2) # Indent -- human readable format
    print(js_str)

def demo_json_encode_text(): # JSON specification supports such format
    print("==== Just text JSON encode ====")
    js_str = json.dumps("Hello, World!", ensure_ascii=False, indent=2)
    # Without quotes, this is not a valid JSON format. But it is a valid JSON value. The JSON specification allows for any valid JSON value 
    # to be encoded as a JSON string, including strings, numbers, booleans, null, arrays, and objects. However, when encoding a string as a JSON 
    # value, it must be enclosed in double quotes. If you want to encode a string as a JSON value without quotes, you can use the `json.dumps()` 
    # function with the `ensure_ascii=False` parameter set to `True`. This will encode the string as a JSON value without quotes. However, this is 
    # not recommended as it may lead to confusion and errors when decoding the JSON value later on.
    print(js_str) # "Hello, World!"






def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








