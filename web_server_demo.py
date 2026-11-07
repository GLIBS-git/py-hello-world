'''
    Web server demo Glibs Python scripts
'''
#!/usr/bin/python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, ThreadingHTTPServer, BaseHTTPRequestHandler
import package_demo.glibs_tools as glibs_tools
import sys
import time
import threading
from urllib.parse import urlparse, parse_qs, unquote

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    #simpleWebServer()
    #simpleWebServer_2()
    baseWebServer()
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

class UrlParcer():
    def __init__(self, url: str):
        self.parsed_url = urlparse(url)
        self.path = unquote(self.parsed_url.path)
        self.query_params = parse_qs(self.parsed_url.query)

def baseWebServer():
    print("==== Base Web Server ====")
    class BaseHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            url_parcer = UrlParcer(self.path)
            match url_parcer.path:
                case "/":
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b"Welcome to glibs py-hello-world base REST API web service!")
                case "/ping":
                    delay = 0
                    if 'delay' in url_parcer.query_params:
                        delay_arr = url_parcer.query_params['delay']
                        if len(delay_arr) > 0:
                            delay_str = delay_arr[0]
                            if delay_str.isdigit():
                                delay = int(delay_str)
                    if (delay > 0):
                        time.sleep(delay)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b"glibs py-hello-world base REST API web service is alive!")
                case _:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(f"Endpoint {self.path} is not supported!".encode())
        def do_POST(self):
            url_parcer = UrlParcer(self.path)
            match url_parcer.path:
                case "/shutdown":
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b"Shutting down glibs py-hello-world base REST API web service...")
                    # Run shutdown() in another thread to avoid a deadlock
                    threading.Thread(target=self.server.shutdown, daemon=True).start()   
                case _:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(f"Endpoint {self.path} is not supported!".encode())
    server = ThreadingHTTPServer(('localhost', 5050), BaseHandler)
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








