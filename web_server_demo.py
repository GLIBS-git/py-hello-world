'''
    Web server demo Glibs Python scripts
'''
#!/usr/bin/python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, ThreadingHTTPServer
import package_demo.glibs_tools as glibs_tools
import sys

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    simpleWebServer()
    #simpleWebServer_2()
    #test()

def simpleWebServer():
    print("==== Simple Web Server ====")
    server = HTTPServer(('localhost', 5050), SimpleHTTPRequestHandler)
    print("Starting simple static file web server at http://localhost:5050")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(); print("Stopping server.")
    finally:
        server.server_close()  # Close the server socket

def simpleWebServer_2():
    print("==== Threaded Web Server ====")
    server = ThreadingHTTPServer(('localhost', 5050), SimpleHTTPRequestHandler)
    print("Starting threaded web server at http://localhost:5050")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(); print("Stopping server.")
    finally:
        server.server_close()  # Close the server socket



def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








