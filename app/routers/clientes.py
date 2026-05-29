from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.cliente_schema import ClienteCreate
from app.services.cliente_service import ClienteService

router = APIRouter(
    tags=["Clientes"]
)


@router.post(
    "/clientes",
    status_code=201
)
def criar_cliente(
    payload: ClienteCreate,
    db: Session = Depends(get_db)
):
    return ClienteService.create_cliente(
        db,
        payload
    )