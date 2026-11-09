'''
    Base Web server demo Glibs Python scripts
'''
#!/usr/bin/python3
from http.server import ThreadingHTTPServer
import package_demo.glibs_base_tools as base_tools
import package_demo.glibs_web_server_tools as web_tools
import os
import sys
import time
import threading

def main(_args):
    menu()

def menu():
    base_tools.clear_console()    
    baseWebServer()
    #test()

def baseWebServer():
    print("==== Base Web Server ====")

    class BaseHandler(web_tools.RestApiHttpHandler):
        def do_GET(self):
            self.init(doLog=True)
            # GET /
            if len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "":
                web_tools.response_ok(self, "Welcome to glibs py-hello-world base REST API web service!")
            # GET /ping
            elif len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "ping":
                delay = 0
                if 'delay' in self.urlParser.query_params:
                    delay_arr = self.urlParser.query_params['delay']
                    if len(delay_arr) > 0:
                        delay_str = delay_arr[0]
                        if delay_str.isdigit():
                            delay = int(delay_str)
                if (delay > 0):
                    time.sleep(delay)
                web_tools.response_ok(self, {"pingResult": "glibs py-hello-world base REST API web service is alive!"})
            # GET /pwd
            elif len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "pwd":
                web_tools.response_ok(self, {"currentDirectory": os.getcwd()})
            else:
                web_tools.response_notFound(self, 'GET')
        def do_POST(self):
            self.init(doLog=True)
            # POST /shutdown
            if len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "shutdown":
                web_tools.response_ok(self, {"message": "Shutting down glibs py-hello-world base REST API web service..."})
                # Run shutdown() in another thread to avoid a deadlock
                threading.Thread(target=self.server.shutdown, daemon=True).start()   
            else:
                web_tools.response_notFound(self, 'POST')

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








