from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.webhook_schema import PipefyWebhook
from app.services.webhook_service import WebhookService

router = APIRouter(
    tags=["Webhooks"]
)


@router.post(
    "/webhooks/pipefy/card-updated",
    status_code=200
)
def processar_webhook(
    payload: PipefyWebhook,
    db: Session = Depends(get_db)
):
    return WebhookService.process_webhook(
        db,
        payload
    )