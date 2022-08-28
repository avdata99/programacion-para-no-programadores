"""
Este script ejecuta un servidor web de prueba en http://localhost:8090/
El servidor se ejecuta correctamente pero la funcion suma y resta no
están funcionando como se espera

Tareas: 
 - Corregir las funciones suma y resta para que entreguen los
   resultados esperados
 - Si los parámetros no son los esperados, lanzar (raise) un
   error para que este se vea en pantalla (en rojo)
 - Agregar la funcion multiplicar
"""


from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8090

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # obtener las partes de la URL
        partes_url = self.path.split('/')
        try:
            content = self.process_url(partes_url)
        except Exception as e:
            content = f'<p style="color:red; font-weigth:bold">ERROR: {e}</p>'

        html = f"""
        <html>
            <head>
                <title>My Server</title>
            </head>
            <body>
                <p>Request: <b>{self.path}</b></p>
                <p>{content}</p>
                <small>Partes: {partes_url}</small>
                <p>This is an example web server.</p>
            </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf-8"))

    def process_url(self, lista_partes):
        """ Devolver el contenido para mostrar """

        if lista_partes[1] == ['']:
            return "<h2>Home page</h2>"
        elif lista_partes[1] == 'suma':
            if len(lista_partes) < 4:
                return "<p>Funcion suma: No hay dos numeros en la URL. Use de la forma /suma/n1/n2</p>"
            else:
                return f"<p>Suma: {lista_partes[2]}+{lista_partes[3]} = {lista_partes[2] + lista_partes[3]}</p>"
        elif lista_partes[1] == 'resta':
            if len(lista_partes) < 4:
                return "<p>Funcion resta: No hay dos numeros en la URL. Use de la forma /resta/n1/n2</p>"
            else:
                return f"<p>Resta: {lista_partes[2]}-{lista_partes[3]} = {lista_partes[2] - lista_partes[3]}</p>"
        else:
            raise ValueError('URL no esperada')


webServer = HTTPServer((HOST, PORT), MyServer)
print(f"Server started at http;//{HOST} {PORT}")

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")
