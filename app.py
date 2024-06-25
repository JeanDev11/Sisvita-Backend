from flask import Flask
from utils.db import db
from services.usuario import usuarios
from services.test import test_bp
from services.nivel_test import nivel_test
from services.test_resultado import test_resultado
from config import DATABASE_CONNECTION
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la extensión SQLAlchemy con la aplicación Flask
db.init_app(app)

# Cargar todos los blueprints
app.register_blueprint(usuarios)
app.register_blueprint(test_bp)
app.register_blueprint(nivel_test)
app.register_blueprint(test_resultado)

with app.app_context():
    # Crea todas las tablas definidas en los modelos
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
