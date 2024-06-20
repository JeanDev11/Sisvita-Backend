from flask import Blueprint, request, jsonify
from utils.db import db
from model.cita import Cita

cita_blueprint = Blueprint('cita', __name__)

@cita_blueprint.route('/cita/insert', methods=['POST'])
def insert_cita():
    result = {}
    body = request.get_json()
    especialista_id = body.get('especialista_id')
    paciente_id = body.get('paciente_id')
    fecha_hora = body.get('fecha_hora')
    asunto = body.get('asunto')
    estado = body.get('estado')

    if not especialista_id or not paciente_id or not fecha_hora or not asunto or not estado:
        result["status_code"] = 400
        result["msg"] = "Faltan datos obligatorios"
        return jsonify(result), 400
    
    try:
        nueva_cita = Cita(
            especialista_id=especialista_id,
            paciente_id=paciente_id,
            fecha_hora=fecha_hora,
            asunto=asunto,
            estado=estado
        )
        
        db.session.add(nueva_cita)
        db.session.commit()
        
        result["data"] = {
            "cita_id": nueva_cita.cita_id,
            "especialista_id": nueva_cita.especialista_id,
            "paciente_id": nueva_cita.paciente_id,
            "fecha_hora": nueva_cita.fecha_hora,
            "asunto": nueva_cita.asunto,
            "estado": nueva_cita.estado
        }
        result["status_code"] = 201
        result["msg"] = "Cita agregada correctamente"
        return jsonify(result), 201
    except Exception as e:
        db.session.rollback()
        result["status_code"] = 500
        result["msg"] = f"Error al agregar la cita: {str(e)}"
        return jsonify(result), 500

@cita_blueprint.route('/cita/get', methods=['GET'])
def get_citas():
    result = {}
    try:
        citas = Cita.query.all()
        result["data"] = [
            {
                "cita_id": cita.cita_id,
                "especialista_id": cita.especialista_id,
                "paciente_id": cita.paciente_id,
                "fecha_hora": cita.fecha_hora,
                "asunto": cita.asunto,
                "estado": cita.estado
            } for cita in citas
        ]
        result["status_code"] = 200
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener citas: {str(e)}"
        return jsonify(result), 500
