from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import clientes, webhooks


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mundo Invest API",
    description="API de gerenciamento de clientes integrada ao fluxo Pipefy",
    version="1.0.0"
)

app.include_router(clientes.router)
app.include_router(webhooks.router)