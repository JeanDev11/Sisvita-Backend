from flask import Blueprint, request, jsonify
from model.nivel_test import NivelTest

nivel_test = Blueprint('nivel_test', __name__)

@nivel_test.route('/nivel_test/obtener_nivel', methods=['POST'])
def obtener_nivel():
    # Obtener el puntaje y el ID del test de la solicitud
    puntaje = request.json.get('puntaje')
    test_id = request.json.get('test_id')

    # Verificar si se proporcionaron los datos necesarios
    if not puntaje or not test_id:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    # Buscar el nivel de ansiedad correspondiente al puntaje y el ID del test
    nivel_ansiedad = NivelTest.query.filter(
        NivelTest.min_puntos <= puntaje,
        NivelTest.max_puntos >= puntaje,
        NivelTest.test_id == test_id
    ).first()

    if nivel_ansiedad:
        # Devolver la descripción del nivel de ansiedad encontrado
        return jsonify({'descripcion': nivel_ansiedad.descripcion})
    else:
        # Devolver un error si no se encontró un nivel de ansiedad correspondiente
        return jsonify({'error': 'No se encontró un nivel de ansiedad correspondiente'}), 404