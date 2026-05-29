import logging

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError

from app.core.database import Base, engine
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler
)

from app.routers import clientes, webhooks

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mundo Invest API",
    description="API de gerenciamento de clientes integrada ao Pipefy",
    version="1.0.0"
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)


@app.get("/")
def root():

    return {
        "message": "Mundo Invest API online"
    }


app.include_router(clientes.router)
app.include_router(webhooks.router)