from flask import Blueprint, request, jsonify
from model.ubigeo import Ubigeo

ubigeo_bp = Blueprint('ubigeo', __name__)

@ubigeo_bp.route('/ubigeo/getall', methods=['GET'])
def get_ubigeoAll():
    result = {}
    try:
        ubigeos = Ubigeo.query.all()
        result = [
            {
                "id_ubigeo": ubigeo.id_ubigeo,
                "departamento": ubigeo.departamento,
                "provincia": ubigeo.provincia,
                "distrito": ubigeo.distrito,
            } for ubigeo in ubigeos
        ]
        return jsonify(result), 200
    except Exception as e:
        result["status_code"] = 500
        result["msg"] = f"Error al obtener ubigeos: {str(e)}"
        return jsonify(result), 500
