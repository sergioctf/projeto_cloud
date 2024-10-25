# Projeto Cloud - Aplicação Flask com Autenticação e Consulta de Dados Externos - 2024.2
**Autor: Sérgio Carmelo**

Bem-vindo ao **Projeto Cloud**, uma aplicação web desenvolvida com o framework Flask em Python. Esta aplicação permite que os usuários se cadastrem, façam login e consultem dados externos atualizados regularmente. Os dados exibidos são obtidos da API pública da CoinGecko, mostrando os preços atuais de criptomoedas como Bitcoin e Ethereum.

**PARA TESTAR: VÁ DIRETO PARA EXECUTAR NO DOCKER**

---

## Índice
1. [Descrição do Projeto](#descrição-do-projeto)
2. [Funcionalidades](#funcionalidades)
3. [Pré-requisitos](#pré-requisitos)
4. [Instalação](#instalação)
5. [Configuração](#configuração)
6. [Como Executar a Aplicação](#como-executar-a-aplicação)
7. [Como Usar a Aplicação Local](#como-usar-a-aplicação)
   - [Login de Usuário](#login-de-usuário)
   - [Consulta de Dados](#consulta-de-dados)
   - [Logout](#logout)
8. [Estrutura do Projeto](#estrutura-do-projeto)
9. [Tecnologias Utilizadas](#tecnologias-utilizadas)
10. [Como Executar a Aplicação com Docker](#docker)
    - [Docker Pré-requisitos](#docker-pré-requisitos)
    - [Como Executar a Aplicação com Docker Compose](#como-executar-a-aplicação-com-docker-compose)
    - [Link para o Docker Hub do Projeto](#link-para-o-docker-hub-do-projeto)

---

## Descrição do Projeto
O **Projeto Cloud** é uma aplicação web simples que demonstra:
- **Autenticação de usuários**: Registro, login e logout.
- **Proteção de rotas**: Apenas usuários autenticados podem acessar a rota de consulta de dados.
- **Integração com API externa**: Consulta de dados atualizados de criptomoedas através da API pública da CoinGecko.
- **Uso de banco de dados**: Armazenamento seguro de informações de usuários utilizando PostgreSQL.
- **Boas práticas de segurança**: Hashing de senhas, uso de tokens JWT para autenticação, gerenciamento de sessões, etc.

## Funcionalidades
- **Registro de Usuário**: Permite que novos usuários se cadastrem fornecendo nome, email e senha.
- **Login de Usuário**: Usuários cadastrados podem fazer login fornecendo email e senha.
- **Consulta de Dados Externos**: Usuários autenticados podem consultar os preços atuais de criptomoedas.
- **Logout**: Usuários podem encerrar a sessão de forma segura.
- **Mensagens de Feedback**: A aplicação fornece mensagens de sucesso e erro para melhorar a experiência do usuário.

## Pré-requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados em seu ambiente:
- **Python 3.7 ou superior**
- **pip** (gerenciador de pacotes do Python)
- **PostgreSQL** (servidor de banco de dados)
- **Git** (opcional, para clonar o repositório)

## Instalação
### 1. Clone o Repositório
```bash
git clone https://github.com/sctcarmelo/projeto_cloud.git
```
### 2. Crie um Ambiente Virtual
```bash
cd projeto_cloud
python -m venv venv

venv\Scripts\activate # Windows

source venv/bin/activate # Linux

```

### 3. Instale as Dependências
```bash

pip install -r requirements.txt
```

### 4. Crie um Banco de Dados PostgreSQL
- Crie um banco de dados no PostgreSQL com o nome `projeto_cloud`.
- Configure as variáveis de ambiente `DATABASE_URL` e `SECRET_KEY` no arquivo `.env`.

```bash
CREATE DATABASE projeto_cloud;
```

## Como Executar a Aplicação
### 1. Inicie o Servidor Flask

```bash
python app.py
```

### 2. Acesse a Aplicação

Abra o navegador e acesse `http://localhost:5000` ou `http://127.0.0.1:5000/`.

# Como Usar a Aplicação

## Registro de Usuário
1. **Acesse a Página de Registro**  
   Na página inicial, clique em **Registrar**.

2. **Preencha o Formulário de Registro**
   - **Nome**: Seu nome completo.
   - **Email**: Um email válido (será usado para login).
   - **Senha**: Crie uma senha segura.
   - Clique em **Registrar**.  
   Se os dados estiverem corretos, você receberá uma mensagem de sucesso e será redirecionado para a página de login.

## Login de Usuário
1. Acesse a **Página de Login** e preencha o formulário com seu email e senha cadastrados.
2. Clique em **Entrar**.

## Consulta de Dados
Após o login, você será redirecionado automaticamente para a página de consulta, que exibirá os preços atuais de criptomoedas.

## Logout
Clique em **Logout** para sair da sua conta. Você será redirecionado para a página inicial.

# Estrutura do Projeto
```csharp
projeto_cloud/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── models/
│   │   └── user_model.py
│   ├── routes/
│   │   └── auth_routes.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── registrar.html
│       ├── login.html
│       └── consultar.html
├── .env
├── docker-compose.yaml
├── README.md
└── venv/ (ambiente virtual)
```

# Tecnologias Utilizadas

- **Flask**: Framework web em Python.
- **PostgreSQL**: Banco de dados relacional.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **Flask-Login**: Gerenciamento de sessões de usuário.
- **Flask-WTF**: Formulários seguros.
- **Flask-Bcrypt**: Hashing de senhas.
- **Flask-JWT-Extended**: Autenticação com tokens JWT.
- **Requests**: Requisições HTTP.
- **Docker**: Containerização da aplicação.

# Docker

## Docker Pré-requisitos
- **Docker Desktop**: Instalado e em execução.
- **Docker Compose**: Instalado e configurado.

## Como Executar a Aplicação com Docker Compose
1. Clone o repositório e acesse a pasta do projeto.
2. Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente necessárias.

```bash
DATABASE_URL=postgresql://user:password@db:5432/projeto_cloud
SECRET_KEY=your_secret_key
```

3. Execute o comando `docker compose up` para construir e iniciar os containers.

```bash
docker compose up
```

4. Acesse a aplicação.

```bash
http://localhost:5000 ou http://127.0.0.1:5000
```

5. Teste a aplicação

- _Registre_, faça _Login_ e _Consulte_ preços atuais de criptomoedas como Bitcoin e Ethereum.
- [Como Usar a Aplicação Local](#como-usar-a-aplicação)
   - [Login de Usuário](#login-de-usuário)
   - [Consulta de Dados](#consulta-de-dados)
   - [Logout](#logout) 

  
## Link para o Docker Hub do Projeto 

https://hub.docker.com/repository/docker/sctcarmelo/projeto_cloud

## Material de Apoio

https://insper.github.io/computacao-nuvem/projetos_2024-2/2024-2_projeto/


