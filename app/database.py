from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///event.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, nullable=False)
    author = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    last_modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    archived = Column(Boolean, default=False)

def init_db():
    Base.metadata.create_all(engine)

def add_event(subject, author, content):
    session = SessionLocal()
    event = Event(subject=subject, author=author, content=content)
    session.add(event)
    session.commit()
    session.close()

def get_event(archived):
    session = SessionLocal()
    events = session.query(Event).filter_by(archived=archived).order_by(Event.created_at.desc()).all()
    session.close()
    return events

def get_event_forum(archived):
    session = SessionLocal()
    events = session.query(Event).filter_by(archived=archived).order_by(Event.last_modified.desc()).all()
    session.close()
    return events

def edit_event(event_id, content):
    session = SessionLocal()
    event = session.query(Event).filter_by(id=event_id).first()
    if event:
        event.content = content
        session.commit()
    session.close()

def archive_event(event_id):
    session = SessionLocal()
    event = session.query(Event).filter_by(id=event_id).first()
    if event:
        event.archived = True
        session.commit()
    session.close()

def restore_event(event_id):
    session = SessionLocal()
    event = session.query(Event).filter_by(id=event_id).first()
    if event:
        event.archived = False
        session.commit()
    session.close()

def delete_event(event_id):
    session = SessionLocal()
    event = session.query(Event).filter_by(id=event_id).first()
    if event:
        session.delete(event)
        session.commit()
    session.close()