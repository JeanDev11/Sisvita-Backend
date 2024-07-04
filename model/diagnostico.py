from utils.db import db
from dataclasses import dataclass

@dataclass
class Diagnostico(db.Model):
    __tablename__ = 'diagnostico'
    id_diagnostico = db.Column(db.Integer, primary_key=True)
    id_tipo_diagnostico = db.Column(db.Integer, db.ForeignKey('tiposdiagnostico.id_tipo_diagnostico'), nullable=False)
    fundamentacion_cientifica = db.Column(db.Text, nullable=True)
    
    tipo_diagnostico__rel = db.relationship('TiposDiagnostico', backref='diagnosticos')

    def __init__(self, id_tipo_diagnostico, fundamentacion_cientifica):
        self.id_tipo_diagnostico = id_tipo_diagnostico
        self.fundamentacion_cientifica = fundamentacion_cientifica
