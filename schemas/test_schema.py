from utils.ma import ma
from model.test import Test

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = ('test_id', 'titulo')
