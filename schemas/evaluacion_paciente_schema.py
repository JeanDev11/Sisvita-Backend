# from marshmallow import fields
# from utils.ma import ma
# from schemas.ubigeo_schema import UbigeoSchema
# from model.evaluacion_paciente import EvaluacionPaciente

# class EvaluacionPacienteSchema(ma.Schema):
#     class Meta:
#         model = EvaluacionPaciente
#         fields = ('id_evaluacion', 'id_diagnostico', 'especialista_id')
    # id_evaluacion = fields.Integer()
    # id_diagnostico = fields.Integer()
    # especialista_id = fields.Integer()
    # resultado_id = fields.Integer()
    # fecha_evaluacion = fields.DateTime()
    # fecha_evaluacion = ma.Nested(UbigeoSchema)