from flask import Blueprint, request, jsonify
from model.diagnostico import Diagnostico
from utils.db import db

diagnostico_bp = Blueprint('diagnostico', __name__)

@diagnostico_bp.route('/diagnostico/getall', methods=['GET'])
def get_diagnosticoAll():
#     evaluacionPaciente = EvaluacionPaciente.query.all()

#     evaluacionPacienteSchema_schema = EvaluacionPacienteSchema(many=True)
#     evaluacionPaciente_serializados = evaluacionPacienteSchema_schema.dump(evaluacionPaciente)  # Serializar los resultados

#     return jsonify(evaluacionPaciente_serializados), 200 

    result = {}
    try:
        diagnosticos = Diagnostico.query.all()
        result = [
            {
                "id_diagnostico": d.id_diagnostico,
                "id_tipo_diagnostico": d.id_tipo_diagnostico,
                "fundamentacion_cientifica": d.fundamentacion_cientifica,
            } for d in diagnosticos
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener diagnosticos: {str(e)}"
        return jsonify(result), 500
    

@diagnostico_bp.route('/diagnostico/insert', methods=['POST'])
def insert_diagnostico():
    result = {}
    body = request.get_json()
    id_tipo_diagnostico = body.get('id_tipo_diagnostico')
    fundamentacion_cientifica = body.get('fundamentacion_cientifica')

    if not id_tipo_diagnostico:
        result["status_code"] = 400
        result["msg"] = "Se requiere 'id_tipo_diagnostico'"
        return jsonify(result), 400

    nuevo_diagnostico = Diagnostico(
        id_tipo_diagnostico=id_tipo_diagnostico,
        fundamentacion_cientifica=fundamentacion_cientifica,
    )
    
    db.session.add(nuevo_diagnostico)
    db.session.commit()

    result["data"] = {
        "id_diagnostico": nuevo_diagnostico.id_diagnostico,
        "id_tipo_diagnostico": nuevo_diagnostico.id_tipo_diagnostico,
        "fundamentacion_cientifica": nuevo_diagnostico.fundamentacion_cientifica,
    }
    result["status_code"] = 201
    result["msg"] = "Diagnostico registrado correctamente"
    return jsonify(result), 201