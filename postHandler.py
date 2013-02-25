__author__ = 'Zilvinas Kucinskas'

from BaseHTTPServer import BaseHTTPRequestHandler
from propertiesParser import Properties
import  cgi

HOST = 'host'
PORT = 'port'

class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        # Begin the response
        self.send_response(201)
        self.send_header("Content-type", "application/xml")
        self.send_header("sdeaf-mrf-uniqueId", "0999116")
        self.end_headers()
        self.wfile.write('<data>%s</data>\n' % "lalala")

if __name__ == '__main__':
    p = Properties()
    p.load(open('configuration.properties'))

    host = p[HOST]
    port = int(p[PORT])

    from BaseHTTPServer import HTTPServer
    server = HTTPServer((host, port), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
