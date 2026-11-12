'''
    Base Web server demo Glibs Python scripts
'''
#!/usr/bin/python3
import asyncio
import datetime
from http.server import ThreadingHTTPServer
import os
import package_demo.glibs_base_tools as base_tools
import package_demo.glibs_web_server_tools as web_tools
from pathlib import Path
import sys
import threading

appConfig = {}

class BaseHandler(web_tools.RestApiHttpHandler):
    def do_GET(self):
        self.init(doLog=True)
        # GET /
        if len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "":
            web_tools.response_ok(self, "Welcome to glibs py-hello-world base REST API web service!")
        # GET /help
        elif len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "help":
            helpPath = str(Path(__file__).resolve().parent / "app_data/base_web_server_help.json")
            helpFile = base_tools.ApplicationConfig(helpPath)
            helpText = helpFile.get("endpointList", "No help text found in the help file.")
            web_tools.response_text(self, str(helpText))
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
                asyncio.run(asyncio.sleep(delay))
            web_tools.response_ok(self, {"pingResult": "glibs py-hello-world base REST API web service is alive!"})
        # GET /pwd
        elif len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "pwd":
            web_tools.response_ok(self, {"currentDirectory": os.getcwd()})
        # GET /sys-info
        elif len(self.urlParser.path_list) == 2 and self.urlParser.path_list[1].lower() == "sys-info":
            sysInfo = {
                "platform": sys.platform,
                "pythonVersion": sys.version,
                "executable": sys.executable,
                "scriptPath": __file__,}
            web_tools.response_ok(self, {"sysInfo": sysInfo})
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
    # Read application configuration from JSON file
    global appConfig
    confPath = str(Path(__file__).resolve().parent / "app_data/base_web_server_config.json")
    appConfig = base_tools.ApplicationConfig(confPath)
    serverAddr = appConfig.get("webServerAddress")
    serverAddr = serverAddr if isinstance(serverAddr, dict) else {}
    serverHost = serverAddr.get("host", "localhost")
    serverPort = serverAddr.get("port", 5050)
    # Start Web server
    server = ThreadingHTTPServer((serverHost, serverPort), BaseHandler)
    print(f"{datetime.date.today()}: Starting threaded web server at http://{serverHost}:{serverPort}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(); print(f"{datetime.date.today()}: Stopping server...")
    finally:
        server.server_close()  # Close the server socket

def main(_args):
    base_tools.clear_console()    
    runBaseWebServer()
    #test()


def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








