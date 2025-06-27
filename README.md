# Encurtador de URL Full-stack (`url-encurtador-fullstack`)

![Status](https://img.shields.io/badge/status-concluído-green)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-blue?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-blue?logo=react&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql&logoColor=white)

Um serviço completo de encurtamento de URLs, construído com uma arquitetura moderna e desacoplada. Este projeto demonstra a criação de uma API RESTful robusta com FastAPI, um frontend reativo com React, e a orquestração de serviços com Docker Compose, seguindo as melhores práticas de desenvolvimento.

## 🎯 Sobre o Projeto

O objetivo deste projeto foi construir uma aplicação web full-stack funcional e escalável, simulando um ambiente de desenvolvimento profissional. A arquitetura foi projetada para ser modular, com uma clara separação de responsabilidades entre o frontend, o backend e o banco de dados, todos executando em containers Docker isolados.

## ✨ Features Principais

-   🔗 **Encurtamento de URL:** Gera um código curto e único para qualquer URL longa.
-   ✏️ **Apelidos Customizados:** Permite que os usuários escolham seus próprios apelidos para os links (ex: `meu-link-secreto`).
-   📊 **Analytics de Cliques:** Rastreia e exibe o número de vezes que cada link encurtado foi acessado.
-   🚀 **Redirecionamento Rápido:** Utiliza redirecionamentos HTTP eficientes (`302 Found`) para garantir a contagem de cliques e uma boa experiência de usuário.
-   🔒 **Segurança:** As configurações sensíveis (como senhas de banco de dados) são gerenciadas através de variáveis de ambiente, seguindo as melhores práticas de segurança.

## 🛠️ Tecnologias Utilizadas

| Camada      | Tecnologia                                                                                                             |
| :---------- | :--------------------------------------------------------------------------------------------------------------------- |
| **Backend** | Python 3.11, FastAPI, SQLAlchemy, Uvicorn, Pydantic                                                                    |
| **Frontend**| React, Vite, JavaScript (JSX), CSS                                                                                     |
| **Banco de Dados**| MySQL 8.0                                                                                                              |
| **Infra & DevOps** | Docker, Docker Compose, Nginx                                                                                        |

## 📂 Estrutura de Pastas

O projeto é organizado em dois diretórios principais, representando a arquitetura desacoplada:

```
url-encurtador-fullstack/
├── url_shortener/          # Projeto Backend (API FastAPI)
└── url-shortener-frontend/ # Projeto Frontend (React)
```

## 🚀 Como Rodar o Projeto Localmente

Este projeto é 100% containerizado, tornando sua execução extremamente simples.

### Pré-requisitos
-   [Docker](https://www.docker.com/products/docker-desktop/)
-   [Docker Compose](https://docs.docker.com/compose/) (já vem com o Docker Desktop)
-   [Git](https://git-scm.com/)

### Passos para Execução

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/inlus/url-encurtador-fullstack.git](https://github.com/inlus/url-encurtador-fullstack.git)
    cd url-encurtador-fullstack
    ```

2.  **Configure as Variáveis de Ambiente do Backend:**
    -   Navegue até a pasta do backend: `cd url_shortener`.
    -   Copie o arquivo de exemplo `.env.example` para um novo arquivo chamado `.env`.
        ```bash
        cp .env.example .env
        ```
    -   Abra o arquivo `.env` e defina uma senha segura para `MYSQL_PASSWORD`.

3.  **Suba os Containers:**
    -   Ainda na pasta `url_shortener/`, execute o Docker Compose. O comando precisa ser rodado desta pasta para que ele encontre o `docker-compose.yml`.
        ```bash
        docker compose up --build
        ```
    -   Este comando irá construir as imagens e iniciar os 3 containers (API, Banco de Dados e Frontend). Aguarde até que os logs se estabilizem.

4.  **Acesse a Aplicação:**
    -   Abra seu navegador e acesse a interface do usuário: [**http://localhost:8080**](http://localhost:8080)
    -   A documentação interativa da API (gerada pelo FastAPI/Swagger) estará disponível em: [**http://localhost:8000/docs**](http://localhost:8000/docs)

## 🔀 Endpoints da API

Aqui estão os principais endpoints disponíveis:

| Método | Rota                  | Descrição                                         |
| :----- | :-------------------- | :------------------------------------------------ |
| `POST` | `/shorten`            | Cria uma nova URL encurtada (normal ou customizada). |
| `GET`  | `/{short_code}`       | Redireciona para a URL longa correspondente.      |
| `GET`  | `/stats/{short_code}` | Retorna os detalhes e estatísticas de um link.      |

---

Feito por **[Luis Felipe Costa]**.

[https://www.linkedin.com/in/luis-felipe-costa-pedro/] | [inlusive22@gmail.com]
