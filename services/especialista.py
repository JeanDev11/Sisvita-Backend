from flask import Blueprint, request, jsonify
from model.especialista import Especialista

especialista_bp = Blueprint('especialista', __name__)

@especialista_bp.route('/especialista/<int:usuario_id>', methods=['GET'])
def get_especialista(usuario_id):
    especialista = Especialista.query.filter_by(usuario_id=usuario_id).first()
    if especialista:
        return jsonify({
            'especialista_id': especialista.especialista_id,
            'usuario_id': especialista.usuario_id,
            'especialidad': especialista.especialidad,
            'nro_colegiado': especialista.nro_colegiado,
            'direccion_consultorio': especialista.direccion_consultorio
        })
    else:
        return jsonify({'message': 'Especialista no encontrado'}), 404