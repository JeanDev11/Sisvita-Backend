from flask import Blueprint, request, jsonify
from model.tipos_diagnostico import TiposDiagnostico

tiposdiagnostico_bp = Blueprint('tiposdiagnostico', __name__)

@tiposdiagnostico_bp.route('/tiposdiagnostico/getall', methods=['GET'])
def get_tiposDiagnosticoAll():
    result = {}
    try:
        tiposDiagnosticos = TiposDiagnostico.query.all()
        result = [
            {
                "id_tipo_diagnostico": td.id_tipo_diagnostico,
                "nombre_diagnostico": td.nombre_diagnostico,
            } for td in tiposDiagnosticos
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener tratamientos: {str(e)}"
        return jsonify(result), 500