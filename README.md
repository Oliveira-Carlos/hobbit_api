# Hobbit API

Bem-vindo à **Hobbit API**, uma aplicação baseada no universo de J.R.R. Tolkien. Este projeto é uma API RESTful desenvolvida com Python e FastAPI, projetada para gerenciar dados de personagens, itens e muito mais.

## Funcionalidades

-   **Gerenciamento de personagens**:
    -   Listar personagens
    -   Criar novos personagens
    -   Atualizar informações de personagens
    -   Remover personagens
-   **Autenticação**:
    -   Registro de usuários
    -   Login com geração de JWT para autenticação

## Tecnologias utilizadas

-   **Linguagem**: Python 3.11+
-   **Framework**: FastAPI
-   **Banco de dados**: PostgreSQL
-   **ORM**: SQLAlchemy
-   **Autenticação**: JWT (JSON Web Tokens)
-   **Outros**:
    -   `<span>python-multipart</span>` para suporte a formulários
    -   `<span>python-dotenv</span>` para gerenciamento de variáveis de ambiente

## Requisitos

Antes de iniciar, certifique-se de que você possui os seguintes itens instalados:

-   Python 3.11+
-   PostgreSQL
-   Git
-   Ambiente virtual configurado (opcional, mas recomendado)

## Instalação

### 1. Clone o repositório

```
git clone https://github.com/Oliveira-Carlos/hobbit_api.git
cd hobbit_api
```

### 2. Configure o ambiente virtual

Crie e ative um ambiente virtual:

```
python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `<span>.env</span>` na raiz do projeto e adicione as seguintes variáveis:

```
# Em breve, instruções detalhadas
```

### 5. Inicialize o banco de dados

Certifique-se de que o PostgreSQL está em execução e execute as migrações para criar as tabelas necessárias:

```
# Em breve, instruções detalhadas sobre migrações
```

### 6. Execute a aplicação

Inicie o servidor de desenvolvimento:

```
uvicorn main:app --reload
```

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Uso da API

### Documentação interativa

Após iniciar a aplicação, você pode acessar a documentação interativa em:

-   Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
-   Redoc: [http://127.0.0.1:8000/redoc]()

### Endpoints principais

#### Cadastro de usuário

-   **POST /register**: Registra um novo usuário
    -   Parâmetros: `<span>username</span>`, `<span>password</span>`

#### Login

-   **POST /login**: Autentica o usuário e retorna um `<span>access_token</span>`
    -   Parâmetros: `<span>username</span>`, `<span>password</span>`

#### Gerenciamento de personagens

-   **GET /characters/**: Lista todos os personagens
-   **POST /characters/**: Cria um novo personagem
    -   Parâmetros: `<span>name</span>`, `<span>race</span>`, `<span>quote</span>` (opcional), `<span>description</span>` (opcional)
-   **PUT /characters/{character_id}**: Atualiza um personagem existente
-   **DELETE /characters/{character_id}**: Remove um personagem

## Contribuição

Este projeto ainda está em desenvolvimento.

## Roadmap

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `<span>LICENSE</span>` para mais informações.

---

Criado com dedicação por [Carlos Oliveira](https://github.com/Oliveira-Carlos).
