from flask import Flask
from utils.db import db
from config import DATABASE_CONNECTION
from flask_cors import CORS
from services.usuario import usuarios_bp
from services.test import test_bp
from services.nivel_test import nivel_test
from services.test_resultado import test_resultado
from services.ubigeo import ubigeo_bp
from services.especialista import especialista_bp
from services.tipos_tratamiento import tipostratamiento_bp
from services.tipos_diagnostico import tiposdiagnostico_bp
from services.diagnostico import diagnostico_bp
from services.tratamiento import tratamiento_bp
from services.evaluacion_paciente import evaluacionpaciente_bp

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la extensión SQLAlchemy con la aplicación Flask
db.init_app(app)

# Cargar todos los blueprints
app.register_blueprint(usuarios_bp)
app.register_blueprint(test_bp)
app.register_blueprint(nivel_test)
app.register_blueprint(test_resultado)
app.register_blueprint(ubigeo_bp)
app.register_blueprint(especialista_bp)
app.register_blueprint(tipostratamiento_bp)
app.register_blueprint(tiposdiagnostico_bp)
app.register_blueprint(diagnostico_bp)
app.register_blueprint(tratamiento_bp)
app.register_blueprint(evaluacionpaciente_bp)

with app.app_context():
    # Crea todas las tablas definidas en los modelos
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
