# app/Dockerfile

# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Instalar bash e netcat (opcional, se não for mais usar o wait-for-it.sh)
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que a aplicação irá rodar
EXPOSE 5000

# Definir a variável de ambiente para indicar o ambiente de produção
ENV FLASK_ENV=production

# Comando para iniciar a aplicação com Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
