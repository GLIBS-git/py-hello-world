'''
    Glibs Python scripts web server tools
'''
#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs, unquote

# Response processors
def response_notFound(handler: BaseHTTPRequestHandler, method: str): # Status 404 text
    handler.send_response(404)
    handler.send_header('Content-type', 'text/plain; charset=utf-8')
    handler.end_headers()
    handler.wfile.write(f"Endpoint '{unquote(urlparse(handler.path).path)}' is not supported for method {method}!".encode('utf-8'))

def response_ok(handler: BaseHTTPRequestHandler, resp_text: str): # Status 200 JSON
    handler.send_response(200)
    handler.send_header('Content-type', 'application/json; charset=utf-8')
    handler.end_headers()
    handler.wfile.write(json.dumps(resp_text, ensure_ascii=False).encode('utf-8'))

def response_text(handler: BaseHTTPRequestHandler, resp_text: str): # Status 200 text
    handler.send_response(200)
    handler.send_header('Content-type', 'text/plain; charset=utf-8')
    handler.end_headers()
    handler.wfile.write(resp_text.encode('utf-8'))

class UrlParcer():
    def __init__(self, url: str):
        self.parsed_url = urlparse(url)
        self.path = unquote(self.parsed_url.path)
        self.path_list = self.path.split('/')
        self.query_params = parse_qs(self.parsed_url.query)

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


















