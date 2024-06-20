from utils.db import db
from dataclasses import dataclass

@dataclass
class Test(db.Model):
    __tablename__ = 'test'
    test_id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descripcion = db.Column(db.String(255))
    rango_puntuacion = db.Column(db.Integer)

    def __init__(self, test_id, titulo, descripcion, rango_puntuacion):
        self.test_id = test_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.rango_puntuacion = rango_puntuacion