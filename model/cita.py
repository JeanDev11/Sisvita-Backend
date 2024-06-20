from utils.db import db
from dataclasses import dataclass

@dataclass
class Cita(db.Model):
    __tablename__ = 'citas'
    cita_id = db.Column(db.Integer, primary_key=True)
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialistas.especialista_id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.paciente_id'))
    fecha_hora = db.Column(db.DateTime)
    asunto = db.Column(db.String(255))
    estado = db.Column(db.String(1))
    paciente = db.relationship('Paciente', backref='citas')
    especialista = db.relationship('Especialista', backref='citas')

    def __init__(self, especialista_id, paciente_id, fecha_hora, asunto, estado):
        self.especialista_id = especialista_id
        self.paciente_id = paciente_id
        self.fecha_hora = fecha_hora
        self.asunto = asunto
        self.estado = estado