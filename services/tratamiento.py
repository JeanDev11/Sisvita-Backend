from flask import Blueprint, request, jsonify
from model.tratamiento import Tratamiento
from utils.db import db

tratamiento_bp = Blueprint('tratamiento', __name__)

@tratamiento_bp.route('/tratamiento/getall', methods=['GET'])
def get_tratamientoAll():
#     evaluacionPaciente = EvaluacionPaciente.query.all()

#     evaluacionPacienteSchema_schema = EvaluacionPacienteSchema(many=True)
#     evaluacionPaciente_serializados = evaluacionPacienteSchema_schema.dump(evaluacionPaciente)  # Serializar los resultados

#     return jsonify(evaluacionPaciente_serializados), 200 

    result = {}
    try:
        tratamientos = Tratamiento.query.all()
        result = [
            {
                "id_tratamiento": t.id_tratamiento,
                "id_tipo_tratamiento": t.id_tipo_tratamiento,
                "id_diagnostico": t.id_diagnostico,
            } for t in tratamientos
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener tratamientos: {str(e)}"
        return jsonify(result), 500
    

@tratamiento_bp.route('/tratamiento/insert', methods=['POST'])
def insert_tratamiento():
    result = {}
    body = request.get_json()
    id_tipo_tratamiento = body.get('id_tipo_tratamiento')
    id_diagnostico = body.get('id_diagnostico')

    if not id_tipo_tratamiento or not id_diagnostico:
        result["status_code"] = 400
        result["msg"] = "Se requiere 'id_tipo_diagnostico'"
        return jsonify(result), 400

    nuevo_tratamiento = Tratamiento(
        id_tipo_tratamiento=id_tipo_tratamiento,
        id_diagnostico=id_diagnostico,
    )
    
    db.session.add(nuevo_tratamiento)
    db.session.commit()

    result["data"] = {
        "id_tipo_tratamiento": nuevo_tratamiento.id_tipo_tratamiento,
        "id_diagnostico": nuevo_tratamiento.id_diagnostico,
    }
    result["status_code"] = 201
    result["msg"] = "Tratamiento registrado correctamente"
    return jsonify(result), 201