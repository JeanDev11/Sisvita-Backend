from flask import Blueprint, request, jsonify
from model.evaluacion_paciente import EvaluacionPaciente
from utils.db import db

evaluacionpaciente_bp = Blueprint('evaluacionpaciente', __name__)

@evaluacionpaciente_bp.route('/evaluacionpaciente/getall', methods=['GET'])
def get_evaluacionPacienteAll():
    result = {}
    try:
        evaluacionPacientes = EvaluacionPaciente.query.all()
        result = [
            {
                "id_tipo_diagnostico": ep.id_tipo_diagnostico,
                "nombre_diagnostico": ep.nombre_diagnostico,
            } for ep in evaluacionPacientes
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener tratamientos: {str(e)}"
        return jsonify(result), 500
    

@evaluacionpaciente_bp.route('/evaluacionpaciente/insert', methods=['POST'])
def insert_evaluacionPaciente():
    result = {}
    body = request.get_json()
    id_diagnostico = body.get('id_diagnostico')
    especialista_id = body.get('especialista_id')
    resultado_id = body.get('resultado_id')

    if not id_diagnostico or not especialista_id or not resultado_id:
        result["status_code"] = 400
        result["msg"] = "Faltan datos obligatorios"
        return jsonify(result), 400

    nuevo_evaluacionPaciente = EvaluacionPaciente(
        id_diagnostico=id_diagnostico,
        especialista_id=especialista_id,
        resultado_id=resultado_id,
    )
    
    db.session.add(nuevo_evaluacionPaciente)
    db.session.commit()

    result["data"] = {
        "id_diagnostico": nuevo_evaluacionPaciente.id_diagnostico,
        "especialista_id": nuevo_evaluacionPaciente.especialista_id,
        "resultado_id": nuevo_evaluacionPaciente.resultado_id,
    }
    result["status_code"] = 201
    result["msg"] = "Evaluacion de paciente registrado correctamente"
    return jsonify(result), 201