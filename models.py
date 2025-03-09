from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine

Base = declarative_base()

# Many-to-Many Association Table
game_genre_association = Table(
    'game_genre', Base.metadata,
    Column('game_id', Integer, ForeignKey('games.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer)

    details = relationship("GameDetails", uselist=False, back_populates="game")
    genres = relationship("Genre", secondary=game_genre_association, back_populates="games")

class GameDetails(Base):
    __tablename__ = 'game_details'

    id = Column(Integer, primary_key=True)
    bio = Column(String)
    platform = Column(String)
    game_id = Column(Integer, ForeignKey('games.id'))

    game = relationship("Game", back_populates="details")

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    games = relationship("Game", secondary=game_genre_association, back_populates="genres")

# Database connection and table creation
engine = create_engine("sqlite:///videogames_collection.db")
Base.metadata.create_all(engine)
