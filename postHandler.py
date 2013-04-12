__author__ = 'Zilvinas Kucinskas'

from BaseHTTPServer import BaseHTTPRequestHandler
from propertiesParser import Properties
from urlparse import parse_qs
import  cgi
import json

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

        content_len = int(self.headers.getheader('content-length'))

        post_body = self.headers.getheader('myurl')

        value_array = json.loads(post_body)
        print value_array['url']
        urlas = value_array['url']
        with open ('myfile', 'w') as f: f.write (urlas)
        # Begin the response
        self.send_response(201)
        self.send_header("Content-type", "application/json")
        #self.send_header("sdeaf-mrf-uniqueId", "0999116")
        self.end_headers()
        self.wfile.write('{%s}' % '"id": "12345"')

if __name__ == '__main__':
    p = Properties()
    p.load(open('configuration.properties'))

    host = p[HOST]
    port = int(p[PORT])

    from BaseHTTPServer import HTTPServer
    server = HTTPServer((host, port), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
