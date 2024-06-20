from utils.db import db
from dataclasses import dataclass

@dataclass
class Paciente(db.Model):
    __tablename__ = 'pacientes'
    paciente_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), unique=True, nullable=False)
    ciclo = db.Column(db.Integer)
    facultad = db.Column(db.String(255))
    carrera = db.Column(db.String(255))
    usuario = db.relationship('Usuario', backref=db.backref('paciente_info', uselist=False))

    def __init__(self, usuario_id, ciclo, facultad, carrera):
        self.usuario_id = usuario_id
        self.ciclo = ciclo
        self.facultad = facultad
        self.carrera = carrera
