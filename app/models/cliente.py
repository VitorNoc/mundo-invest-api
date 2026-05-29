from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime, UTC

from app.core.database import Base


class Cliente(Base):

    __tablename__ = "clientes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    cliente_nome = Column(
        String,
        nullable=False
    )

    cliente_email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    tipo_solicitacao = Column(
        String,
        nullable=False
    )

    valor_patrimonio = Column(
        Float,
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default="Aguardando Análise"
    )

    prioridade = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )