CREATE_CARD_MUTATION = """
mutation CreateCard($input: CreateCardInput!) {
  createCard(input: $input) {
    card {
      id
      title
    }
  }
}
"""


UPDATE_CARD_FIELD_MUTATION = """
mutation UpdateCardField($input: UpdateCardFieldInput!) {
  updateCardField(input: $input) {
    card {
      id
    }
  }
}
"""


class PipefyClient:

    PIPE_ID = "12345"

    PRIORIDADE_FIELD_ID = "prioridade"

    @staticmethod
    def simulate_create_card(cliente):

        return {
            "query": CREATE_CARD_MUTATION,
            "variables": {
                "input": {
                    "pipe_id": PipefyClient.PIPE_ID,
                    "fields_attributes": [
                        {
                            "field_id": "cliente_nome",
                            "field_value": cliente.cliente_nome
                        },
                        {
                            "field_id": "cliente_email",
                            "field_value": cliente.cliente_email
                        },
                        {
                            "field_id": "valor_patrimonio",
                            "field_value": str(
                                cliente.valor_patrimonio
                            )
                        }
                    ]
                }
            }
        }

    @staticmethod
    def simulate_update_card(
        card_id,
        prioridade
    ):

        return {
            "query": UPDATE_CARD_FIELD_MUTATION,
            "variables": {
                "input": {
                    "card_id": card_id,
                    "field_id": PipefyClient.PRIORIDADE_FIELD_ID,
                    "new_value": prioridade
                }
            }
        }