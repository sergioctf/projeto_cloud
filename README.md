# Projeto Cloud - Aplicação Flask com Autenticação e Consulta de Dados Externos - 2024.2
**Autor: Sérgio Carmelo**

Bem-vindo ao **Projeto Cloud**, uma aplicação web desenvolvida com o framework Flask em Python. Esta aplicação permite que os usuários se cadastrem, façam login e consultem dados externos atualizados regularmente. Os dados exibidos são obtidos da API pública da CoinGecko, mostrando os preços atuais de criptomoedas como Bitcoin e Ethereum.

**PARA TESTAR: VÁ DIRETO PARA EXECUTAR NO DOCKER OU NO KUBERNETES**

---

## Índice
1. [Descrição do Projeto](#descrição-do-projeto)
2. [Funcionalidades](#funcionalidades)
3. [Pré-requisitos](#pré-requisitos)
4. [Instalação](#instalação)
5. [Configuração](#configuração)
6. [Como Executar a Aplicação](#como-executar-a-aplicação)
   - [Execução Local com Docker Compose](#execução-local-com-docker-compose)
   - [Execução no Kubernetes (AWS EKS)](#execução-no-kubernetes-aws-eks)
7. [Como Usar a Aplicação](#como-usar-a-aplicação)
   - [Registro de Usuário](#registro-de-usuário)
   - [Login de Usuário](#login-de-usuário)
   - [Consulta de Dados](#consulta-de-dados)
   - [Logout](#logout)
8. [Estrutura do Projeto](#estrutura-do-projeto)
9. [Tecnologias Utilizadas](#tecnologias-utilizadas)
10. [Links Úteis](#links-úteis)
    - [Link para o Docker Hub do Projeto](#link-para-o-docker-hub-do-projeto)
    - [Vídeo Demonstrativo Docker](#vídeo-demonstrativo-docker)
    - [Vídeo Demonstrativo Final](#vídeo-demonstrativo-final)
    - [Material de Apoio](#material-de-apoio)

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

### Para Execução Local com Docker:
- **Docker Desktop**: Instalado e em execução.
- **Docker Compose**: Instalado e configurado.

### Para Execução no Kubernetes (AWS EKS):
- **AWS CLI**: Instalado e configurado com as credenciais apropriadas.
- **kubectl**: Instalado e configurado para interagir com seu cluster EKS.
- **eksctl**: Instalado para gerenciar o cluster EKS.

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
cd /app
pip install -r requirements.txt
```

### 4. Crie um Banco de Dados PostgreSQL
- Crie um banco de dados no PostgreSQL com o nome `projeto_cloud`.
- Configure as variáveis de ambiente `DATABASE_URL` e `SECRET_KEY` no arquivo `.env`.

```bash
CREATE DATABASE projeto_cloud;
```

## Como Executar a Aplicação
- **Você pode executar a aplicação de duas maneiras:**
   - **Localmente com Docker Compose**
   - **No Kubernetes (AWS EKS)**

   ### Execução Local com Docker Compose
   ```bash
   docker-compose up
   ```
   - Acesse a aplicação em `http://localhost:5000` ou `http://127.0.0.1:5000/`.

   ### Execução no Kubernetes (AWS EKS)
   ```bash
   eksctl create cluster --name projeto-cloud-cluster --region us-east-1 --nodegroup-name linux-nodes --node-type t3.medium --nodes 2 --nodes-min 1 --nodes-max 3 --managed
   ```

   ```bash
   kubectl apply -f k8s/db-deployment.yaml
   kubectl apply -f k8s/db-service.yaml
   kubectl apply -f k8s/app-deployment.yaml
   kubectl apply -f k8s/app-service.yaml
   ```
   - Acesse a aplicação em `http://<EXTERNAL-IP>/`.

   ### Meu IP Externo
   ```bash
   http://ad73d793d0cc94384b6f23e832105906-2002410674.us-east-1.elb.amazonaws.com/

## Como Usar a Aplicação
### Registro de Usuário
1. **Acesse a Página de Registro**
   - Na página inicial, clique em **Registrar**.

2. **Preencha o Formulário de Registro**
   - **Nome**: Seu nome completo.
   - **Email**: Um email válido (será usado para login).
   - **Senha**: Crie uma senha segura.
   - Clique em **Registrar**.

3. **Mensagem de Sucesso**
   - Se os dados estiverem corretos, você receberá uma mensagem de sucesso e será redirecionado para a página de login.

### Login de Usuário
1. **Acesse a Página de Login** e preencha o formulário com seu email e senha cadastrados.
2. Clique em **Entrar**.

### Consulta de Dados
- Após o login, você será redirecionado automaticamente para a página de consulta, que exibirá os preços atuais de criptomoedas.

### Logout
- Clique em **Logout** para sair da sua conta. Você será redirecionado para a página inicial.

## Estrutura do Projeto
```
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
├── k8s/ 
│   ├── db-deployment.yaml
│   ├── db-service.yaml
│   ├── app-deployment.yaml
│   └── app-service.yaml
├── README.md
└── venv/ (ambiente virtual)
```

## Tecnologias Utilizadas
- **Flask**: Framework web em Python.
- **PostgreSQL**: Banco de dados relacional.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **Flask-Login**: Gerenciamento de sessões de usuário.
- **Flask-WTF**: Formulários seguros.
- **Flask-Bcrypt**: Hashing de senhas.
- **Flask-JWT-Extended**: Autenticação com tokens JWT.
- **Requests**: Requisições HTTP.
- **Docker**: Containerização da aplicação.
- **Kubernetes**: Orquestração de containers no cluster.
- **AWS EKS**: Serviço gerenciado de Kubernetes na AWS.

## Links Úteis

### Link para o Docker Hub do Projeto
[https://hub.docker.com/repository/docker/sctcarmelo/projeto_cloud](https://hub.docker.com/repository/docker/sctcarmelo/projeto_cloud)

### Vídeo Demonstrativo Docker
[Vídeo Etapa 1](https://youtu.be/E5G2vybC24s)

### Vídeo Demonstrativo Final
[Vídeo Etapa 2]

### Material de Apoio
[https://insper.github.io/computacao-nuvem/projetos_2024-2/2024-2_projeto/](https://insper.github.io/computacao-nuvem/projetos_2024-2/2024-2_projeto/)
```



