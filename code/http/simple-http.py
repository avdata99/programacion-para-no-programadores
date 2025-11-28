from http.server import BaseHTTPRequestHandler, HTTPServer


class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(b"<b>Titulo</b><br>")
        self.wfile.write(b"Hola")
        return


print('starting server...')

httpd = HTTPServer(
    server_address=('0.0.0.0', 8082),
    RequestHandlerClass=Servidor
)

print('Server available at http://0.0.0.0:8082')
httpd.serve_forever()