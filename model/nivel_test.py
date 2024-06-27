from utils.db import db
from dataclasses import dataclass

@dataclass
class NivelTest(db.Model):
    __tablename__ = 'nivel_test'
    id_nivel = db.Column(db.Integer, primary_key=True)
    min_puntos = db.Column(db.Integer)
    max_puntos = db.Column(db.Integer)
    descripcion = db.Column(db.String(255))
    semaforo = db.Column(db.String(50))
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id', onupdate='RESTRICT', ondelete='RESTRICT'))

    def __init__(self, id_nivel, min_puntos, max_puntos, descripcion, semaforo, test_id):
        self.id_nivel = id_nivel
        self.min_puntos = min_puntos
        self.max_puntos = max_puntos
        self.descripcion = descripcion
        self.semaforo = semaforo
        self.test_id = test_id