# test_connection.py
import psycopg2

host = "localhost"
database = "projeto_api"
user = "postgres"
password = "Carmelo282"

print(f"Host: {repr(host)}")
print(f"Database: {repr(database)}")
print(f"User: {repr(user)}")
# Não imprima a senha por segurança

try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        options='-c lc_messages=en_US.UTF-8'
    )
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar: {e}")
