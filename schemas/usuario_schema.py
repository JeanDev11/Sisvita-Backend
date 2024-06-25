from marshmallow import fields
from utils.ma import ma

class UsuarioSchema(ma.Schema):
    usuario_id = fields.Integer()
    nombres = fields.String()
    apellidos = fields.String()
    # correo_electronico = fields.Email()
    # fecha_nac = fields.Date(format='%Y-%m-%d')
