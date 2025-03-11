
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import click
from models import Base, Game, GameDetails, Genre

# Database setup
DATABASE_URL = "sqlite:///games.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Ensure tables are created
Base.metadata.create_all(engine)

@click.group()
def cli():
    """CLI for Video Games Management"""
    pass

# Add a new game
@click.command()
@click.option('--game_id', type=int, help="Game ID (optional, auto-generated if not provided)")
@click.option('--name', prompt='Game Title')
@click.option('--year', prompt="Game Year of Production", type=int)
def add_game(game_id, name, year):
    """Adds a new game to the collection"""
    session = SessionLocal()

    # If game_id is provided, use it; otherwise, let the database assign one
    if game_id:
        game = Game(id=game_id, title=name, year=year)
    else:
        game = Game(title=name, year=year)

    session.add(game)
    session.commit()
    click.echo(f"New game added: ID {game.id}, Title '{game.title}' ({game.year})")
    session.close()

#  Add or update game details
@click.command()
@click.option('--game_id', prompt='Game ID', type=int)
@click.option('--details', prompt="Game Details")
@click.option('--platform', prompt="Game Platform")
@click.option('--genre', prompt="Game Genre")
def add_game_details(game_id, details, platform, genre):
    """Adds or updates details for an existing game"""
    session = SessionLocal()
    game = session.query(Game).filter(Game.id == game_id).first()

    if not game:
        click.echo("Game not found.")
        session.close()
        return

    if game.details:
        game.details.bio = details
        game.details.platform = platform
    else:
        game.details = GameDetails(bio=details, platform=platform, game=game)
        session.add(game.details)

    genre_obj = session.query(Genre).filter(Genre.name == genre).first()
    if not genre_obj:
        genre_obj = Genre(name=genre)
        session.add(genre_obj)

    if genre_obj not in game.genres:
        game.genres.append(genre_obj)

    session.commit()
    click.echo(f"Updated details for {game.title}: {details} (Platform: {platform}, Genre: {genre})")
    session.close()

# View all games
@click.command()
def list_games():
    """Lists all games and their details"""
    session = SessionLocal()
    games = session.query(Game).all()

    if not games:
        click.echo("No games found.")
        session.close()
        return

    click.echo("\n  Your Video Games Collection:\n")
    for game in games:
        genres = ', '.join([genre.name for genre in game.genres]) if game.genres else "None"
        details = f" Details: {game.details.bio} | Platform: {game.details.platform}" if game.details else "No additional details available."
        rank = game.rank if hasattr(game, 'rank') else "Not Ranked"
        click.echo(f" {game.id}: {game.title} ({game.year})\n    Genres: {genres}\n   {details}\n    Rank: {rank}\n")
    
    session.close()

#  Edit a game
@click.command()
@click.option('--game_id', prompt='Game ID', type=int)
@click.option('--new_title', prompt='New Game Title', default=None)
@click.option('--new_year', prompt='New Year of Production', type=int, default=None)
def edit_game(game_id, new_title, new_year):
    """Edits game title or year"""
    session = SessionLocal()
    game = session.query(Game).filter(Game.id == game_id).first()

    if not game:
        click.echo("Game not found.")
        session.close()
        return

    if new_title:
        game.title = new_title
    if new_year:
        game.year = new_year

    session.commit()
    click.echo(f" Game updated: {game.title} ({game.year})")
    session.close()

#  Rank a game
@click.command()
@click.option('--game_id', prompt='Game ID', type=int)
@click.option('--rank', prompt='Rank (1-10)', type=int)
def rank_game(game_id, rank):
    """Ranks a game from 1 to 10"""
    if rank < 1 or rank > 10:
        click.echo(" Rank must be between 1 and 10.")
        return

    session = SessionLocal()
    game = session.query(Game).filter(Game.id == game_id).first()

    if not game:
        click.echo(" Game not found.")
        session.close()
        return

    game.rank = rank  # Assuming Game model has 'rank' column
    session.commit()
    click.echo(f" {game.title} ranked {rank}/10")
    session.close()

# Sort games
@click.command()
@click.option('--by', prompt='Sort by (title/year/rank)', type=click.Choice(['title', 'year', 'rank']))
def sort_games(by):
    """Sorts games by title, year, or rank"""
    session = SessionLocal()
    order_column = getattr(Game, by, None)

    if order_column is None:
        click.echo(" Invalid sort option.")
        session.close()
        return

    games = session.query(Game).order_by(order_column).all()

    if not games:
        click.echo(" No games found.")
        session.close()
        return

    click.echo(f"\n Games sorted by {by}:\n")
    for game in games:
        click.echo(f" {game.title} ({game.year}) - Rank: {game.rank if hasattr(game, 'rank') else 'Not Ranked'}")
    
    session.close()

#  Delete a game
@click.command()
@click.option('--game_id', prompt='Game ID', type=int)
def delete_game(game_id):
    """Deletes a game from the collection"""
    session = SessionLocal()
    game = session.query(Game).filter(Game.id == game_id).first()

    if not game:
        click.echo(" Game not found.")
        session.close()
        return

    session.delete(game)
    session.commit()
    click.echo(f" Deleted {game.title}")
    session.close()

# Register commands
cli.add_command(add_game)
cli.add_command(add_game_details)
cli.add_command(list_games)
cli.add_command(edit_game)
cli.add_command(rank_game)
cli.add_command(sort_games)
cli.add_command(delete_game)

if __name__ == '__main__':
    cli()
