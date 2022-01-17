from typing import Collection
from sqlalchemy import create_engine
from sqlalchemy import text, select
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import registry, relationship
from sqlalchemy import Column, Table, Integer, String, SmallInteger, ForeignKey, ARRAY

from secrets import DB_URI


engine = create_engine(DB_URI)
mapper_registry = registry()
Base = mapper_registry.generate_base()


class Artist(Base):
    __tablename__ = 'artists'

    id = Column("artist_id", SmallInteger, primary_key=True)
    name = Column("artist_name", String, nullable=False)
    artist_genres = Column("artist_genres", ARRAY(String))
    popularity = Column("artist_popularity", SmallInteger)
    image = Column("artist_image", String)
    banner = Column("artist_banner", String, nullable=True)


class Albums(Base):
    __tablename__ = 'albums'

    id = Column(SmallInteger, primary_key=True)
    artist_id = Column(SmallInteger, ForeignKey("artists.id"), nullable=False)
    name = Column(String, nullable=False)
    

# mapper_registry.metadata.create_all(engine)

session = Session(engine)


stmt = select(Artist).where(Artist.name == 'Demi Lovato')

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)


session.commit()
