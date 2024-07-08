from flask import Blueprint, request, jsonify
from model.usuario import Usuario
from model.paciente import Paciente
from model.especialista import Especialista
from utils.db import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from schemas.usuario_schema import UsuarioSchema
import jwt
import datetime

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios/insert', methods=['POST'])
def insert_usuario():
    result = {}
    body = request.get_json()
    nombres = body.get('nombres')
    apellidos = body.get('apellidos')
    correo_electronico = body.get('correo_electronico')
    contrasena = body.get('contrasena')
    rol = body.get('rol')
    es_paciente = body.get('es_paciente', False)
    telefono = body.get('telefono')
    dni = body.get('dni')
    fecha_nac = body.get('fecha_nac')
    sexo = body.get('sexo')
    id_ubigeo = body.get('id_ubigeo')
    if not nombres or not apellidos or not correo_electronico or not contrasena or not rol or not dni or not id_ubigeo:
        result["status_code"] = 400
        result["msg"] = "Faltan datos obligatorios"
        return jsonify(result), 400
    
    contrasena_hashed = generate_password_hash(contrasena)
    
    nuevo_usuario = Usuario(
        nombres=nombres,
        apellidos=apellidos,
        correo_electronico=correo_electronico,
        contrasena=contrasena_hashed,
        rol=rol,
        es_paciente=es_paciente,
        telefono=telefono,
        dni=dni,
        fecha_nac=fecha_nac,
        sexo=sexo,
        id_ubigeo=id_ubigeo,
    )
    
    db.session.add(nuevo_usuario)
    db.session.commit()

    if rol == 'P':
        ciclo = body.get('ciclo')
        facultad = body.get('facultad')
        carrera = body.get('carrera')

        if not ciclo or not facultad or not carrera:
            result["status_code"] = 400
            result["msg"] = "Faltan datos específicos del paciente"
            return jsonify(result), 400

        nuevo_paciente = Paciente(
            usuario_id=nuevo_usuario.usuario_id,
            ciclo=ciclo,
            facultad=facultad,
            carrera=carrera
        )
        
        db.session.add(nuevo_paciente)

    elif rol == 'E':
        especialidad = body.get('especialidad')
        nro_colegiado = body.get('nro_colegiado')
        direccion_consultorio = body.get('direccion_consultorio')

        if not especialidad or not nro_colegiado:
            result["status_code"] = 400
            result["msg"] = "Faltan datos específicos del especialista"
            return jsonify(result), 400

        nuevo_especialista = Especialista(
            usuario_id=nuevo_usuario.usuario_id,
            especialidad=especialidad,
            nro_colegiado=nro_colegiado,
            direccion_consultorio=direccion_consultorio
        )
        
        db.session.add(nuevo_especialista)

    db.session.commit()

    result["data"] = {
        "usuario_id": nuevo_usuario.usuario_id,
        "nombres": nuevo_usuario.nombres,
        "apellidos": nuevo_usuario.apellidos,
        "correo_electronico": nuevo_usuario.correo_electronico,
        "rol": nuevo_usuario.rol
    }
    result["status_code"] = 201
    result["msg"] = "Usuario registrado correctamente"
    return jsonify(result), 201

@usuarios_bp.route('/usuarios/getall', methods=['GET'])
def get_usuariosAll():
    usuarios = Usuario.query.all()  # Obtener todos los usuarios desde la base de datos

    usuario_schema = UsuarioSchema(many=True)  # Inicializar el esquema para serializar múltiples usuarios
    usuarios_serializados = usuario_schema.dump(usuarios)  # Serializar los resultados

    return jsonify(usuarios_serializados), 200  # Devolver los usuarios serializados como JSON

@usuarios_bp.route('/usuarios/login', methods=['POST'])
def login_usuario():
    result = {}
    body = request.get_json()
    correo_electronico = body.get('correo_electronico')
    contrasena = body.get('contrasena')

    if not correo_electronico or not contrasena:
        result["status_code"] = 400
        result["msg"] = "Faltan correo electrónico o contraseña"
        return jsonify(result), 400

    usuario = Usuario.query.filter_by(correo_electronico=correo_electronico).first()

    if not usuario:
        result["status_code"] = 404
        result["msg"] = "Usuario no encontrado"
        return jsonify(result), 404

    if not check_password_hash(usuario.contrasena, contrasena):
        result["status_code"] = 401
        result["msg"] = "Credenciales inválidas"
        return jsonify(result), 401

    token = generate_token(usuario.usuario_id)

    result["data"] = {
        "usuario_id": usuario.usuario_id,
        "nombres": usuario.nombres,
        "apellidos": usuario.apellidos,
        "correo_electronico": usuario.correo_electronico,
        "rol": usuario.rol,
        "token": token
    }
    result["status_code"] = 200
    result["msg"] = "Inicio de sesión exitoso"
    return jsonify(result), 200

@usuarios_bp.route('/usuarios/update', methods=['PUT'])
def update_usuario():
    result = {}
    body = request.get_json()
    token = request.headers.get('Authorization').split(" ")[1]
    user_id = decode_token(token)

    if not user_id:
        result["status_code"] = 401
        result["msg"] = "Token inválido o expirado"
        return jsonify(result), 401

    usuario = Usuario.query.filter_by(usuario_id=user_id).first()
    if not usuario:
        result["status_code"] = 404
        result["msg"] = "Usuario no encontrado"
        return jsonify(result), 404

    contrasena_actual = body.get('contrasena_actual')
    if not check_password_hash(usuario.contrasena, contrasena_actual):
        result["status_code"] = 401
        result["msg"] = "Contraseña actual incorrecta"
        return jsonify(result), 401

    # Solo actualizar los campos que no estén vacíos
    nombres = body.get('nombres')
    if nombres:
        usuario.nombres = nombres

    apellidos = body.get('apellidos')
    if apellidos:
        usuario.apellidos = apellidos

    telefono = body.get('telefono')
    if telefono:
        usuario.telefono = telefono

    fecha_nac = body.get('fecha_nac')
    if fecha_nac:
        usuario.fecha_nac = fecha_nac

    sexo = body.get('sexo')
    if sexo:
        usuario.sexo = sexo

    contrasena_nueva = body.get('contrasena_nueva')
    if contrasena_nueva:
        usuario.contrasena = generate_password_hash(contrasena_nueva)

    db.session.commit()

    result["status_code"] = 200
    result["msg"] = "Datos actualizados correctamente"
    return jsonify(result), 200

@usuarios_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
def get_Usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)

    result = {
        'nombres': usuario.nombres,
        'apellidos': usuario.apellidos,
        'telefono': usuario.telefono,
        'fecha_nac': usuario.fecha_nac.strftime('%Y-%m-%d'),
        'sexo': usuario.sexo,
    }
    
    return jsonify(result)


# Define una clave secreta para firmar los tokens
SECRET_KEY = 'sisvita_key_g9'

# Función para generar un token JWT
def generate_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Función para verificar un token JWT
def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None