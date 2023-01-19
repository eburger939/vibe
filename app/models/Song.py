from datetime import datetime
from app.db import Base
from .vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    song_url = Column(String(100), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    vibe_id = Column(Integer, ForeignKey('vibes.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User')
    vibe = relationship('Vibe')
    vote_count = column_property(
        select([func.count(Vote.id)]).where(Vote.song_id==id)
    )
    votes = relationship('Vote', cascade='all,delete')