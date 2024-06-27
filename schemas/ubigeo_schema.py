from utils.ma import ma
from model.ubigeo import Ubigeo

class UbigeoSchema(ma.Schema):
    class Meta:
        model = Ubigeo
        fields = ('id_ubigeo', 'departamento', 'latitud', 'longitud')