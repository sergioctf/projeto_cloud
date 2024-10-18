# routes/data_routes.py

from flask import Blueprint, jsonify, request
from functools import wraps
import jwt
import os
import requests

data_bp = Blueprint('data', __name__)

# Carregar a chave secreta das variáveis de ambiente
SECRET_KEY = os.getenv('SECRET_KEY', 'sua_chave_secreta')

# Decorador para verificar o token JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Verificar se o token está no header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1] if " " in auth_header else auth_header

        if not token:
            return jsonify({'message': 'Token é necessário!'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user_id = data['id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido!'}), 401

        return f(current_user_id, *args, **kwargs)
    return decorated

@data_bp.route('/consultar', methods=['GET'])
@token_required
def consultar(current_user_id):
    # Aqui você fará a requisição aos dados de terceiros
    # Exemplo: Obter dados de câmbio do dólar

    try:
        # Exemplo de API pública (utilize uma API que não exija chave de API)
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        if response.status_code != 200:
            return jsonify({'message': 'Erro ao obter dados externos.'}), 500

        data = response.json()
        # Retornar apenas algumas informações
        return jsonify({
            'base': data['base'],
            'date': data['date'],
            'rates': data['rates']
        }), 200
    except Exception as e:
        return jsonify({'message': 'Erro ao obter dados externos.', 'error': str(e)}), 500
