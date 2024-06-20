from utils.db import db
from dataclasses import dataclass

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialistas'
    especialista_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), unique=True, nullable=False)
    especialidad = db.Column(db.String(255), nullable=False)
    nro_colegiado = db.Column(db.Integer)
    direccion_consultorio = db.Column(db.String(255))
    usuario = db.relationship('Usuario', backref=db.backref('especialista_info', uselist=False))

    def __init__(self, usuario_id, especialidad, nro_colegiado, direccion_consultorio):
        self.usuario_id = usuario_id
        self.especialidad = especialidad
        self.nro_colegiado = nro_colegiado
        self.direccion_consultorio = direccion_consultorio

