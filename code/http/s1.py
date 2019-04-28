"""
Hello World vía web local
https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Template
import os


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        carpeta = os.path.dirname(os.path.abspath(__file__))
        path = '{}/templates{}'.format(carpeta, self.path)
        f = open(path, 'r')
        template = Template(f.read())
        f.close()
        context = {'python_version': self.sys_version}
        message = template.render(context)
        
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


print('starting server...')

# Server settings
# Choose port 8080, for port 80, which is normally used for a http server, you need root access
server_address = ('127.0.0.1', 8081)
httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
print('running server...')
httpd.serve_forever()