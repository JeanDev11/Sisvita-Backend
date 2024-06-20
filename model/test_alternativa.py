from utils.db import db
from dataclasses import dataclass

@dataclass
class TestAlternativa(db.Model):
    __tablename__ = 'test_alternativa'
    alternativa_id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('test_pregunta.pregunta_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    alternativa = db.Column(db.String(255))
    puntaje = db.Column(db.Integer)

    def __init__(self, alternativa_id, pregunta_id, alternativa, puntaje):
        self.alternativa_id = alternativa_id
        self.pregunta_id = pregunta_id
        self.alternativa = alternativa
        self.puntaje = puntaje