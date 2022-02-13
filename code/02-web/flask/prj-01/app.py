from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Flask World'


@app.route("/user/<string:user_name>/")
def show_user(user_name):
    return f"Mostrando datos del usuario {user_name}"

"""
(opcionalmente ejecutar export FLASK_ENV=development para que los cambios se apliquen sin reiniciar el servidor)
Ejecutar "flask run" desde la linea de comandos

* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Ir al navegador e ingresar a http://127.0.0.1:5000/

En la linea de comandos queda regisro de esa visita
127.0.0.1 - - [22/Jan/2022 11:54:52] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Jan/2022 11:54:52] "GET /favicon.ico HTTP/1.1" 404 -
"""
