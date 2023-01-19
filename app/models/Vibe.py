from datetime import datetime
from app.db import Base
from .vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property


class Vibe(Base):
    __tablename__ = 'vibes'
    id = Column(Integer, primary_key=True)
    vibe_name = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User')
    songs = relationship('Song', cascade='all,delete')
