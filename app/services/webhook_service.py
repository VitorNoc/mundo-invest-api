import logging

from fastapi import HTTPException

from app.repositories.event_repository import EventRepository
from app.repositories.cliente_repository import ClienteRepository
from app.clients.pipefy_client import PipefyClient

logger = logging.getLogger(__name__)


class WebhookService:

    @staticmethod
    def process_webhook(db, payload):

        existing_event = EventRepository.exists(
            db,
            payload.event_id
        )

        if existing_event:
            raise HTTPException(
                status_code=409,
                detail="Evento já processado"
            )

        cliente = ClienteRepository.get_by_email(
            db,
            payload.cliente_email
        )

        if not cliente:
            raise HTTPException(
                status_code=404,
                detail="Cliente não encontrado"
            )

        prioridade = (
            "prioridade_alta"
            if cliente.valor_patrimonio >= 200000
            else "prioridade_normal"
        )

        cliente.status = "Processado"
        cliente.prioridade = prioridade

        db.commit()
        db.refresh(cliente)

        EventRepository.create(
            db,
            payload.event_id
        )

        graphql_payload = PipefyClient.simulate_update_card(
            payload.card_id,
            prioridade
        )

        logger.info(
            f"Webhook processado: {cliente.cliente_email}"
        )

        return {
    "message": "Webhook processado com sucesso",
    "cliente": {
        "email": cliente.cliente_email,
        "status": cliente.status,
        "prioridade": prioridade
    },
    "pipefy_payload": graphql_payload
}