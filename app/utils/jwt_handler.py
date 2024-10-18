import jwt
import os
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def generate_token(user):
    payload = {
        'id': user[0],
        'nome': user[1],
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            bearer = request.headers['Authorization']
            token = bearer.split()[1]

        if not token:
            return jsonify({'error': 'Token ausente'}), 403

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = {'id': data['id'], 'nome': data['nome']}
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 403

        return f(current_user, *args, **kwargs)
    return decorated
