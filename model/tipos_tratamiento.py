from utils.db import db
from dataclasses import dataclass

@dataclass
class TiposTratamiento(db.Model):
    __tablename__ = 'tipostratamiento'
    id_tipo_tratamiento = db.Column(db.Integer, primary_key=True)
    nombre_tratamiento = db.Column(db.String(100))

    def __init__(self, id_tipo_tratamiento, nombre_tratamiento):
        self.id_tipo_tratamiento = id_tipo_tratamiento
        self.nombre_tratamiento = nombre_tratamiento