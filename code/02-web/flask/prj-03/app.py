from flask import Flask, render_template
from models.bondis import get_bondis_info, get_bondi_info


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


@app.route("/datos/")
def datos():
    data = get_bondis_info()
    site_title = 'Datos del sistema de transporte de la Ciudad de Córdoba'
    return render_template("datos.html", data=data, site_title=site_title)


@app.route("/bondi/<int:bondi_id>/")
def bondi(bondi_id):
    data = get_bondi_info(bondi_id)
    site_title = 'Info de un solo bondi'
    return render_template("bondi.html", bondi=data, site_title=site_title)
