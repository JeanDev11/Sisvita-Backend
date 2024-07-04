from utils.db import db
from dataclasses import dataclass

@dataclass
class Tratamiento(db.Model):
    __tablename__ = 'tratamiento'
    id_tratamiento = db.Column(db.Integer, primary_key=True)
    id_tipo_tratamiento = db.Column(db.Integer, db.ForeignKey('tipostratamiento.id_tipo_tratamiento'), nullable=False)
    id_diagnostico = db.Column(db.Integer, db.ForeignKey('diagnostico.id_diagnostico'), nullable=False)

    tipo_tratamiento__rel = db.relationship('TiposTratamiento', backref='tratamientos')
    diagnostico__rel = db.relationship('Diagnostico', backref='tratamientos')

    def __init__(self, id_tipo_tratamiento, id_diagnostico):
        self.id_tipo_tratamiento = id_tipo_tratamiento
        self.id_diagnostico = id_diagnostico
