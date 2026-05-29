from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models.cliente import Cliente


class ClienteRepository:

    @staticmethod
    def create(db, payload):

        cliente = Cliente(
            cliente_nome=payload.cliente_nome,
            cliente_email=payload.cliente_email,
            tipo_solicitacao=payload.tipo_solicitacao,
            valor_patrimonio=payload.valor_patrimonio,
            status="Aguardando Análise"
        )

        db.add(cliente)

        try:
            db.commit()

        except IntegrityError:
            db.rollback()

            raise HTTPException(
                status_code=409,
                detail="Cliente já cadastrado"
            )

        db.refresh(cliente)

        return cliente

    @staticmethod
    def get_by_email(db, email):

        return db.query(Cliente).filter(
            Cliente.cliente_email == email
        ).first()