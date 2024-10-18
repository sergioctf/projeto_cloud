import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Configurar o logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserModel:
    def __init__(self):
        host = os.getenv("DB_HOST", "db")
        database = os.getenv("DB_NAME", "projeto_api")
        user = os.getenv("DB_USER", "postgres")
        password = os.getenv("DB_PASSWORD", "")

        try:
            self.connection = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                options='-c lc_messages=en_US.UTF-8'
            )
            self.cursor = self.connection.cursor()
            self.create_table()
            logger.info("Conectado ao banco de dados e tabela verificada/criada.")
        except Exception as e:
            logger.error(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def create_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            senha_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def find_by_email(self, email):
        query = sql.SQL("SELECT * FROM users WHERE email = %s;")
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()

    def find_by_id(self, user_id):
        query = sql.SQL("SELECT * FROM users WHERE id = %s;")
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def insert_user(self, nome, email, senha_hash):
        insert_query = sql.SQL("""
            INSERT INTO users (nome, email, senha_hash)
            VALUES (%s, %s, %s)
            RETURNING id, nome, email, created_at, updated_at;
        """)
        self.cursor.execute(insert_query, (nome, email, senha_hash))
        self.connection.commit()
        return self.cursor.fetchone()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        logger.info("Conexão com o banco de dados fechada.")
