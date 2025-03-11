
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine

Base = declarative_base()

# Many-to-Many Association Table
game_genre_association = Table(
    'game_genre', Base.metadata,
    Column('game_id', Integer, ForeignKey('games.id', ondelete="CASCADE"), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id', ondelete="CASCADE"), primary_key=True)
)

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Ensure IDs auto-increment
    title = Column(String, nullable=False, unique=True)  # Ensure titles are unique
    year = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=True)  # Add rank column

    details = relationship("GameDetails", uselist=False, back_populates="game", cascade="all, delete-orphan")
    genres = relationship("Genre", secondary=game_genre_association, back_populates="games")

class GameDetails(Base):
    __tablename__ = 'game_details'

    id = Column(Integer, primary_key=True)
    bio = Column(String, nullable=True)
    platform = Column(String, nullable=False)
    game_id = Column(Integer, ForeignKey('games.id', ondelete="CASCADE"), unique=True)

    game = relationship("Game", back_populates="details")

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    games = relationship("Game", secondary=game_genre_association, back_populates="genres")

# Database connection and table creation
DATABASE_URL = "sqlite:///games.db"  # Keeping consistent with `main.py`
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
