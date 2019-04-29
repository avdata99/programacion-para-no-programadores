"""
Hello World vía web local
https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Template
import os
import socket
from code.base-de-datos import b1

host = '0.0.0.0'
port = 8082

def get_my_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):
            
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        carpeta = os.path.dirname(os.path.abspath(__file__))
        path = '/index.html' if self.path in ['/', ''] else self.path
        
        full_path = '{}/templates{}'.format(carpeta, path)
        f = open(full_path, 'r')
        template = Template(f.read())
        f.close()
        context = {'python_version': self.sys_version,
                    'direccion': self.client_address,
                    'ip_publica': get_my_ip_address()}
        message = template.render(context)
        
        self.wfile.write(bytes(message, "utf8"))
        return


print('starting server...')

# Server settings
# Choose port 8080, for port 80, which is normally used for a http server, you need root access
# server_address = ('127.0.0.1', 8082)
server_address = (host, port)
httpd = HTTPServer(server_address, Servidor)
print('running server...')
httpd.serve_forever()