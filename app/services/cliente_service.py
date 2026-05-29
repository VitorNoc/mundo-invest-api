from app.repositories.cliente_repository import ClienteRepository
from app.clients.pipefy_client import PipefyClient


class ClienteService:

    @staticmethod
    def create_cliente(db, payload):

        cliente = ClienteRepository.create(
            db,
            payload
        )

        graphql_payload = PipefyClient.simulate_create_card(
            cliente
        )

        return {
            "message": "Cliente criado com sucesso",
            "cliente": {
                "id": cliente.id,
                "nome": cliente.cliente_nome,
                "email": cliente.cliente_email,
                "status": cliente.status
            },
            "pipefy_payload": graphql_payload
        }