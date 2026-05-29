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

# Exemplos de Requisição

## Criar Cliente

```bash
curl -X POST "http://127.0.0.1:8000/clientes" ^
-H "Content-Type: application/json" ^
-d "{\"cliente_nome\":\"João Silva\",\"cliente_email\":\"joao@example.com\",\"tipo_solicitacao\":\"Atualização cadastral\",\"valor_patrimonio\":250000}"
```

---

## Processar Webhook

```bash
curl -X POST "http://127.0.0.1:8000/webhooks/pipefy/card-updated" ^
-H "Content-Type: application/json" ^
-d "{\"event_id\":\"evt_123\",\"card_id\":\"card_456\",\"cliente_email\":\"joao@example.com\",\"timestamp\":\"2026-05-18T12:00:00Z\"}"
```

---

# Visão de Escalabilidade AWS

O projeto foi estruturado pensando em futura escalabilidade utilizando serviços AWS como:

- ECS / Fargate
- RDS PostgreSQL
- API Gateway
- CloudWatch
- SQS para processamento assíncrono
- Lambda para eventos

Essa arquitetura permitiria desacoplamento do processamento de webhooks, maior escalabilidade horizontal e monitoramento centralizado da aplicação.

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