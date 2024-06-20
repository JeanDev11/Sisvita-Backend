from utils.db import db
from dataclasses import dataclass

@dataclass
class TestPregunta(db.Model):
    __tablename__ = 'test_pregunta'
    pregunta_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    texto_pregunta = db.Column(db.String(255))
    orden = db.Column(db.Integer)

    def __init__(self, pregunta_id, test_id, texto_pregunta, orden):
        self.pregunta_id = pregunta_id
        self.test_id = test_id
        self.texto_pregunta = texto_pregunta
        self.orden = orden