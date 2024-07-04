from utils.db import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuario_id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    correo_electronico = db.Column(db.String(255), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(1), nullable=False)  # 'P' para paciente, 'E' para especialista
    es_paciente = db.Column(db.Boolean, default=False)
    telefono = db.Column(db.String(20), nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    fecha_nac = db.Column(db.Date)
    sexo = db.Column(db.String(1))

    # Relación con Ubigeo
    id_ubigeo = db.Column(db.Integer, db.ForeignKey('ubigeo.id_ubigeo', onupdate='RESTRICT', ondelete='RESTRICT'))
    ubigeo = relationship('Ubigeo', back_populates='usuarios')

    def __init__(self, nombres, apellidos, correo_electronico, contrasena, rol, es_paciente, telefono, dni, fecha_nac, sexo, id_ubigeo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.rol = rol
        self.es_paciente = es_paciente
        self.telefono = telefono
        self.dni = dni
        self.fecha_nac = fecha_nac
        self.sexo = sexo
        self.id_ubigeo = id_ubigeo

