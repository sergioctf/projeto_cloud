# app/app.py

from flask import Flask, render_template
from routes.auth_routes import auth_bp
import os
import time
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

# Configurar a chave secreta
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'sua_chave_secreta')

# Registrar o Blueprint
app.register_blueprint(auth_bp)

# Rota para a página inicial
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def create_db_connection():
    attempt = 0
    while attempt < 5:
        try:
            connection = psycopg2.connect(
                host=os.getenv("DB_HOST", "localhost"),
                database=os.getenv("DB_NAME", "projeto_api"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASSWORD", ""),
                options='-c lc_messages=en_US.UTF-8'
            )
            return connection
        except OperationalError as e:
            attempt += 1
            app.logger.warning(f"Falha na conexão com o banco de dados. Tentativa {attempt}/5. Erro: {e}")
            time.sleep(5)
    app.logger.error("Não foi possível conectar ao banco de dados após 5 tentativas.")
    exit(1)

if __name__ == '__main__':
    # Tentar conectar ao banco de dados antes de iniciar a aplicação
    create_db_connection()
    app.run(host='0.0.0.0', port=5000, debug=True)
