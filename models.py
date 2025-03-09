from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship  

Base = declarative_base()

# Many-to-Many Association Table
game_genre_association = Table(
    'game_genre', Base.metadata,
    Column('game_id', Integer, ForeignKey('games.id'), primary_key=True),  # Fixed ForeignKey
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)  # Fixed ForeignKey
)

class Game(Base):
    __tablename__ = 'games'  # Table name should be lowercase

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer)

    # Relationship with GameDetails
    details = relationship("GameDetails", uselist=False, back_populates="game")

    # Many-to-Many Relationship with Genre
    genres = relationship("Genre",  # Fixed case-sensitive issue
                          secondary=game_genre_association,
                          back_populates="games")

class GameDetails(Base):
    __tablename__ = 'game_details'  # Fixed table name

    id = Column(Integer, primary_key=True)
    bio = Column(String)
    platform = Column(String)
    game_id = Column(Integer, ForeignKey('games.id'))  # Fixed ForeignKey reference

    # Relationship with Game
    game = relationship("Game", back_populates="details")

class Genre(Base):
    __tablename__ = 'genres'  # Fixed table name

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Changed 'title' to 'name'

    # Many-to-Many Relationship with Game
    games = relationship("Game",
                         secondary=game_genre_association,
                         back_populates="genres")  # Fixed back_populates reference
