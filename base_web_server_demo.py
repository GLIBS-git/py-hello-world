'''
    Base Web server demo Glibs Python scripts
'''
#!/usr/bin/python3
from http.server import ThreadingHTTPServer
import package_demo.glibs_base_tools as base_tools
import package_demo.glibs_web_server_tools as web_tools
from pathlib import Path
import os
import sys
import time
import threading

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
        # GET /sys-info
        elif len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "sys-info":
            web_tools.response_ok(self, {"programFile": __file__})
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

def runBaseWebServer():
    print("==== Base Web Server ====")
    global appConfig
    confPath = str(Path(__file__).resolve().parent / "app_data/base_web_server_config.json")
    appConfig = base_tools.ApplicationConfig(confPath)
    serverAddr: dict = appConfig.get("webServerAddress", {"host": "localhost", "port": 5050})
    serverHost = serverAddr.get("host", "localhost")
    serverPort = serverAddr.get("port", 5050)
    server = ThreadingHTTPServer((serverHost, serverPort), BaseHandler)
    print(f"Starting threaded web server at http://{serverHost}:{serverPort}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(); print("Stopping server.")
    finally:
        server.server_close()  # Close the server socket

appConfig = {}

def main(_args):
    base_tools.clear_console()    
    runBaseWebServer()
    #test()


def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








