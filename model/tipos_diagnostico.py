from utils.db import db
from dataclasses import dataclass

@dataclass
class TiposDiagnostico(db.Model):
    __tablename__ = 'tiposdiagnostico'
    id_tipo_diagnostico = db.Column(db.Integer, primary_key=True)
    nombre_diagnostico = db.Column(db.String(100))

    def __init__(self, id_tipo_diagnostico, nombre_diagnostico):
        self.id_tipo_diagnostico = id_tipo_diagnostico
        self.nombre_diagnostico = nombre_diagnostico