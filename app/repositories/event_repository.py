from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.processed_event import ProcessedEvent


class EventRepository:

    @staticmethod
    def exists(db, event_id):

        return db.query(ProcessedEvent).filter(
            ProcessedEvent.event_id == event_id
        ).first()

    @staticmethod
    def create(db, event_id):

        event = ProcessedEvent(
            event_id=event_id
        )

        db.add(event)

        try:
            db.commit()

        except IntegrityError:

            db.rollback()

            raise HTTPException(
                status_code=409,
                detail="Evento já processado"
            )

        return event