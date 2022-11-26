from flask import Flask, render_template
from cripto.data import get_price


app = Flask(
    __name__,
    # Carpeta donde se encuentran los archivos estáticos
    static_folder='static',
    # Carpeta donde se encuentran los templates para el frontend
    template_folder='templates'
)


@app.route('/')
def index():
    site_title = 'Mi aplicacion web'
    return render_template("index.html", site_title=site_title)


@app.route("/price/<symbol>")
@app.route("/price/<symbol>/<to_symbol>")
def datos(symbol, to_symbol='USDT'):
    data = get_price(symbol, to_symbol)
    context = {
        'symbol': symbol,
        'to_symbol': to_symbol,
        'data': data,
    }
    site_title = 'Datos del sistema de transporte de la Ciudad de Córdoba'
    return render_template("datos.html", site_title=site_title, **context)
