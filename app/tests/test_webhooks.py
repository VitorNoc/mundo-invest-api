def test_process_webhook(client):

    cliente_payload = {
        "cliente_nome": "Maria Silva",
        "cliente_email": "maria@example.com",
        "tipo_solicitacao": "Investimento",
        "valor_patrimonio": 300000
    }

    client.post(
        "/clientes",
        json=cliente_payload
    )

    webhook_payload = {
        "event_id": "evt_123",
        "card_id": "card_456",
        "cliente_email": "maria@example.com",
        "timestamp": "2026-05-18T12:00:00Z"
    }

    response = client.post(
        "/webhooks/pipefy/card-updated",
        json=webhook_payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Webhook processado com sucesso"

    assert data["cliente"]["email"] == "maria@example.com"

    assert data["cliente"]["status"] == "Processado"

    assert data["cliente"]["prioridade"] == "prioridade_alta"

    assert "pipefy_payload" in data


def test_duplicate_event(client):

    cliente_payload = {
        "cliente_nome": "Carlos",
        "cliente_email": "carlos@example.com",
        "tipo_solicitacao": "Cadastro",
        "valor_patrimonio": 100000
    }

    client.post(
        "/clientes",
        json=cliente_payload
    )

    webhook_payload = {
        "event_id": "evt_duplicate_999",
        "card_id": "card_789",
        "cliente_email": "carlos@example.com",
        "timestamp": "2026-05-18T12:00:00Z"
    }

    first_response = client.post(
        "/webhooks/pipefy/card-updated",
        json=webhook_payload
    )

    second_response = client.post(
        "/webhooks/pipefy/card-updated",
        json=webhook_payload
    )

    assert first_response.status_code == 200

    assert second_response.status_code == 409

    assert (
    second_response.json()["detail"]
    == "Evento já processado"
)