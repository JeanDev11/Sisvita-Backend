from utils.db import db
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class EvaluacionPaciente(db.Model):
    __tablename__ = 'evaluacionpaciente'
    id_evaluacion = db.Column(db.Integer, primary_key=True)
    id_diagnostico = db.Column(db.Integer, db.ForeignKey('diagnostico.id_diagnostico'), nullable=False)
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialistas.especialista_id'), nullable=False)
    resultado_id = db.Column(db.Integer, db.ForeignKey('test_resultado.resultado_id'), nullable=False)
    fecha_evaluacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    diagnostico__rel = db.relationship('Diagnostico', backref='evaluacion_paciente')
    especialista__rel = db.relationship('Especialista', backref='evaluacion_paciente')
    test_resultado__rel = db.relationship('TestResultado', backref='evaluacion_paciente')

    def __init__(self, id_diagnostico, especialista_id, resultado_id, fecha_evaluacion=None):
        self.id_diagnostico = id_diagnostico
        self.especialista_id = especialista_id
        self.resultado_id = resultado_id
        if fecha_evaluacion is None:
            self.fecha_evaluacion = datetime.now(timezone.utc)
        else:
            self.fecha_evaluacion = fecha_evaluacion




# NOTA:
# Usar como guia para las relaciones y el modelado de una clase.