def test_create_cliente(client):

    payload = {
        "cliente_nome": "João Silva",
        "cliente_email": "joao123@example.com",
        "tipo_solicitacao": "Atualização cadastral",
        "valor_patrimonio": 250000
    }

    response = client.post(
        "/clientes",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["message"] == "Cliente criado com sucesso"

    assert data["cliente"]["nome"] == "João Silva"

    assert data["cliente"]["email"] == "joao123@example.com"

    assert data["cliente"]["status"] == "Aguardando Análise"

    assert "pipefy_payload" in data