from flask import Blueprint, jsonify
from model.test import Test
from model.test_pregunta import TestPregunta
from model.test_alternativa import TestAlternativa

test_bp = Blueprint('test_bp', __name__)

@test_bp.route('/tests', methods=['GET'])
def get_tests():
    tests = Test.query.all()
    result = []
    for test in tests:
        result.append({
            'test_id': test.test_id,
            'titulo': test.titulo,
            'descripcion': test.descripcion,
            'rango_puntuacion': test.rango_puntuacion
        })
    return jsonify(result)

@test_bp.route('/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    test = Test.query.get_or_404(test_id)

    result = {
        'test_id': test.test_id,
        'titulo': test.titulo,
        'descripcion': test.descripcion,
        'rango_puntuacion': test.rango_puntuacion
    }
    
    return jsonify(result)

@test_bp.route('/tests/<int:test_id>/preguntas', methods=['GET'])
def get_preguntas(test_id):
    preguntas = TestPregunta.query.filter_by(test_id=test_id).all()
    result = []
    for pregunta in preguntas:
        result.append({
            'pregunta_id': pregunta.pregunta_id,
            'test_id': pregunta.test_id,
            'texto_pregunta': pregunta.texto_pregunta,
            'orden': pregunta.orden
        })
    return jsonify(result)

@test_bp.route('/preguntas/<int:pregunta_id>/alternativas', methods=['GET'])
def get_alternativas(pregunta_id):
    alternativas = TestAlternativa.query.filter_by(pregunta_id=pregunta_id).all()
    result = []
    for alternativa in alternativas:
        result.append({
            'alternativa_id': alternativa.alternativa_id,
            'pregunta_id': alternativa.pregunta_id,
            'alternativa': alternativa.alternativa,
            'puntaje': alternativa.puntaje
        })
    return jsonify(result)
