# app/routes/auth_routes.py

from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models.user_model import UserModel
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os
import requests

auth_bp = Blueprint('auth', __name__)

# Carregar a chave secreta das variáveis de ambiente
SECRET_KEY = os.getenv('SECRET_KEY', 'sua_chave_secreta')

# Inicializar o modelo de usuário
user_model = UserModel()

@auth_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome or not email or not senha:
            flash('Nome, email e senha são obrigatórios.', 'error')
            return redirect(url_for('auth.registrar'))

        # Verificar se o email já está registrado
        if user_model.find_by_email(email):
            flash('Email já registrado.', 'error')
            return redirect(url_for('auth.registrar'))

        # Gerar hash da senha
        senha_hash = generate_password_hash(senha)

        # Inserir o usuário no banco de dados
        try:
            user = user_model.insert_user(nome, email, senha_hash)
            flash('Usuário registrado com sucesso!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'Erro ao registrar usuário: {str(e)}', 'error')
            return redirect(url_for('auth.registrar'))
    else:
        return render_template('registrar.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not email or not senha:
            flash('Email e senha são obrigatórios.', 'error')
            return redirect(url_for('auth.login'))

        user = user_model.find_by_email(email)
        if user and check_password_hash(user[3], senha):
            token = jwt.encode(
                {
                    'id': user[0],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                },
                SECRET_KEY,
                algorithm='HS256'
            )
            # Armazenar o token na sessão
            session['token'] = token
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('auth.consultar'))
        else:
            flash('Credenciais inválidas.', 'error')
            return redirect(url_for('auth.login'))
    else:
        return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('token', None)
    flash('Você foi desconectado.', 'success')
    return redirect(url_for('index'))

@auth_bp.route('/consultar', methods=['GET'])
def consultar():
    token = session.get('token')

    if not token:
        flash('Por favor, faça login para acessar esta página.', 'error')
        return redirect(url_for('auth.login'))

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user = user_model.find_by_id(data['id'])
        if not user:
            flash('Usuário não encontrado.', 'error')
            return redirect(url_for('auth.login'))

        # Obter dados da CoinGecko API
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,brl')
        if response.status_code == 200:
            dados = response.json()
        else:
            dados = {'mensagem': 'Não foi possível obter os dados externos.'}

        return render_template('consultar.html', user={'id': user[0], 'nome': user[1], 'email': user[2]}, dados=dados)
    except jwt.ExpiredSignatureError:
        flash('Sua sessão expirou. Por favor, faça login novamente.', 'error')
        return redirect(url_for('auth.login'))
    except jwt.InvalidTokenError:
        flash('Token inválido. Por favor, faça login novamente.', 'error')
        return redirect(url_for('auth.login'))
