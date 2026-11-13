'''
    Glibs Python scripts web server tools
'''
#!/usr/bin/python3
#from package_demo.glibs_base_tools import ApplicationConfig
from .glibs_base_tools import ApplicationConfig
from http.server import BaseHTTPRequestHandler
import json
import os
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote


# Response processors
def response_notFound(handler: BaseHTTPRequestHandler, method: str): # Status 404 text
    handler.send_response(404)
    handler.send_header('Content-type', 'text/plain; charset=utf-8')
    handler.end_headers()
    handler.wfile.write(f"Endpoint '{unquote(urlparse(handler.path).path)}' is not supported for method {method}!".encode('utf-8'))

def response_ok(handler: BaseHTTPRequestHandler, resp_json): # Status 200 JSON
    handler.send_response(200)
    handler.send_header('Content-type', 'application/json; charset=utf-8')
    handler.end_headers()
    handler.wfile.write(json.dumps(resp_json, ensure_ascii=False).encode('utf-8'))

def response_text(handler: BaseHTTPRequestHandler, resp_text: str): # Status 200 text
    handler.send_response(200)
    handler.send_header('Content-type', 'text/plain; charset=utf-8')
    handler.end_headers()
    handler.wfile.write(resp_text.encode('utf-8'))

def response_json(handler: BaseHTTPRequestHandler, resp_json: dict): # Status 200 JSON
    handler.send_response(200)
    handler.send_header('Content-type', 'application/json; charset=utf-8')
    handler.end_headers()
    handler.wfile.write(json.dumps(resp_json, ensure_ascii=False).encode('utf-8'))


class UrlParcer():
    def __init__(self, url: str):
        self.parsed_url = urlparse(url) # URL to ubject with path and query parameters
        self.path = unquote(self.parsed_url.path) # Decoding encoded symbols like %20 to spaces from the URL path without query parameters
        self.path_list = self.path.split('/') # List of path segments, e.g. /api/v1/resource -> ["", "api", "v1", "resource"]
        self.query_params = parse_qs(self.parsed_url.query) # Dictionary of query parameters


class RestApiHttpHandler(BaseHTTPRequestHandler):

    def init(self, doLog=False):
        self.urlParser = UrlParcer(self.path)
        if doLog:
            print(f"Request: {self.command} {self.path} from {self.client_address[0]}:{self.client_address[1]}")

    def doGet(self, doLog=False):
        response_notFound(self, 'GET')

    def doPost(self, doLog=False):
        response_notFound(self, 'POST')

    def doPut(self, doLog=False):
        response_notFound(self, 'PUT')

    def doDelete(self, doLog=False):
        response_notFound(self, 'DELETE')


class WebAppConfig():

    def __init__(self, filePath: str, confFile: str):
        self.filePath = filePath
        if not os.path.exists(filePath):
            raise FileNotFoundError(f"Base file '{filePath}' does not exist.")
        self.confFile = confFile
        confFile = str(Path(self.filePath).resolve().parent / self.confFile)
        if not os.path.exists(confFile):
            raise FileNotFoundError(f"Configuration file '{confFile}' does not exist.")

    def load(self):
        self.appConfig = ApplicationConfig(self.confFile)
        serverAddr = self.appConfig.get("webServerAddress")
        serverAddr = serverAddr if isinstance(serverAddr, dict) else {}
        self.serverHost = serverAddr.get("host", "localhost")
        self.serverPort = serverAddr.get("port", 5050)


















