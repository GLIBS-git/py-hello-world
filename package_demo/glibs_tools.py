'''
    Glibs Python scripts tools
'''
#!/usr/bin/python3
import os
import subprocess
import sys
from urllib.parse import urlparse, parse_qs, unquote

def main(_args):
    menu()

def menu():
    clear_console()    
    test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
class UrlParcer():
    def __init__(self, url: str):
        self.parsed_url = urlparse(url)
        self.path = unquote(self.parsed_url.path)
        self.path_list = self.path.split('/')
        self.query_params = parse_qs(self.parsed_url.query)




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








