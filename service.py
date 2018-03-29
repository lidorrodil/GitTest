#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from sys import argv
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import argparse

PORT = 1882
#PATH = "/var/lib/service/"
PATH = "E:\\GitTest\\"

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>The amount of POST requests: " + str(get_counter()) + "!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        increase_counter()

     
def run(port, server_class=HTTPServer, handler_class=S):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd...")
    httpd.serve_forever()

def increase_counter():
    filename = PATH + 'counter.dat'

    try:
        # Read the counter post file
        file = open(filename, "r+")
        
        line = file.readlines()

        # Increase the counter
        increase = int(line[0]) + 1

        # Clean the file
        file.seek(0)
        file.truncate()

        # Write the new counter to the file
        file.write(str(increase))

        file.close()

    except ValueError, e:
        print(str(e))
        exit(1)

def get_counter():
    filename = PATH + 'counter.dat'

    # Read the counter post file
    try:
        file = open(filename, "r+")
        line = file.readlines()
        file.close()
        return (int(line[0]))
    except ValueError, e:
        print(str(e))
        exit(1)

if __name__ == "__main__":

    # Define arguments
    parser = \
        argparse.ArgumentParser(description='Helper to Alibaba task.')
    parser.add_argument('-p', '--port',
                        help='Path to the pairs file', required=True)

    # Parse arguments
    args = parser.parse_args()

    port = args.port

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run(int(port))
