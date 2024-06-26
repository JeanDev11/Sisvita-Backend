from utils.ma import ma
from model.nivel_test import NivelTest

class NivelTestSchema(ma.Schema):
    class Meta:
        model = NivelTest
        fields = ('id_nivel', 'descripcion')