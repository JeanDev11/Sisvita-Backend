from flask import Blueprint, request, jsonify
from model.tipos_tratamiento import TiposTratamiento

tipostratamiento_bp = Blueprint('tipostratamiento', __name__)

@tipostratamiento_bp.route('/tipostratamiento/getall', methods=['GET'])
def get_tiposTratamientoAll():
    result = {}
    try:
        tiposTratamientos = TiposTratamiento.query.all()
        result = [
            {
                "id_tipo_tratamiento": tt.id_tipo_tratamiento,
                "nombre_tratamiento": tt.nombre_tratamiento,
            } for tt in tiposTratamientos
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener tratamientos: {str(e)}"
        return jsonify(result), 500
