from sqlalchemy import Column, Integer, String

from app.core.database import Base


class ProcessedEvent(Base):

    __tablename__ = "processed_events"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(
        String,
        unique=True,
        nullable=False
    )