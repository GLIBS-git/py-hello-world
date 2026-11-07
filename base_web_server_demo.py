'''
    Base Web server demo Glibs Python scripts
'''
#!/usr/bin/python3
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import package_demo.glibs_base_tools as base_tools
import package_demo.glibs_web_server_tools as web_tools
import sys
import time
import threading

def main(_args):
    menu()

def menu():
    base_tools.clear_console()    
    baseWebServer()
    #test()

class BaseHandlerBase_Glibs(BaseHTTPRequestHandler):
    def doGet(self):
        web_tools.response_notFound(self, 'GET')
    def doPost(self):
        web_tools.response_notFound(self, 'POST')
    def doPut(self):
        web_tools.response_notFound(self, 'PUT')
    def doDelete(self):
        web_tools.response_notFound(self, 'DELETE')

def baseWebServer():
    print("==== Base Web Server ====")

    class BaseHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            url_parcer = web_tools.UrlParcer(self.path)
            if len(url_parcer.path_list) == 2 and url_parcer.path_list[1].lower() == "":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Welcome to glibs py-hello-world base REST API web service!")
                print(f"Request: {self.command} {self.path} from {self.client_address[0]}:{self.client_address[1]}")
            elif len(url_parcer.path_list) == 2 and url_parcer.path_list[1].lower() == "ping":
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
                print(f"Request: {self.command} {self.path} from {self.client_address[0]}:{self.client_address[1]}")
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"Endpoint '{self.path}' is not supported!".encode())
                print(f"Request: {self.command} {self.path} from {self.client_address[0]}:{self.client_address[1]}")
        def do_POST(self):
            url_parcer = web_tools.UrlParcer(self.path)
            if len(url_parcer.path_list) == 2 and url_parcer.path_list[1].lower() == "shutdown":
                # Run shutdown() in another thread to avoid a deadlock
                threading.Thread(target=self.server.shutdown, daemon=True).start()   
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Shutting down glibs py-hello-world base REST API web service...")
                print(f"Request: {self.command} {self.path} from {self.client_address[0]}:{self.client_address[1]}")
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"Endpoint '{self.path}' is not supported!".encode())
                print(f"Request: {self.command} {self.path} from {self.client_address[0]}:{self.client_address[1]}")

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








