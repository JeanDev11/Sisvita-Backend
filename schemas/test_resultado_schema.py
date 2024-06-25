from utils.ma import ma
from model.test_resultado import TestResultado
from schemas.usuario_schema import UsuarioSchema
from schemas.test_schema import TestSchema
from marshmallow import fields

class TestResultadoSchema(ma.Schema):
    usuario = ma.Nested(UsuarioSchema)
    test = ma.Nested(TestSchema)
    fecha_creacion = fields.DateTime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = TestResultado
        fields = ('resultado_id', 
                  'puntaje_obtenido', 
                  'descripcion', 
                  'fecha_creacion', 
                  'usuario', 
                  'test')
        

testResultado_schema = TestResultadoSchema()
testResultados_schema = TestResultadoSchema(many=True)