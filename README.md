# Mundo Invest API

Backend desenvolvido com FastAPI para gerenciamento de clientes e processamento de webhooks integrados ao Pipefy.

---

# Objetivo

O projeto simula um fluxo backend corporativo utilizado em operações financeiras, realizando:

- Cadastro de clientes
- Processamento de solicitações
- Integração com Pipefy
- Processamento de webhooks
- Controle de eventos duplicados (idempotência)

---

# Tecnologias Utilizadas

- Python 3.14
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Pytest
- GraphQL
- Uvicorn

---

# Arquitetura do Projeto

```text
app/
├── clients/
├── core/
├── models/
├── repositories/
├── routers/
├── schemas/
├── services/
├── tests/
└── main.py