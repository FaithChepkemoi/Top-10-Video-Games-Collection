
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import click
from models import Game, GameDetails, Genre
# Create CLI group
@click.group()
def cli():
    """CLI for Video Games Management"""
    pass

# Command to add a new game
@click.command()
@click.option('--name', prompt='Game Name')
@click.option('--year', prompt="Game Year of production", type=int)
def add_game(name, year):
    session = SessionLocal()
    game = Game(title=name, year=year)  # Changed 'name' to 'title' to match the Game model
    session.add(game)
    session.commit()
    click.echo(f"New game added: {game.title}")
    session.close()

def add_gameDetails():
    pass

def add_genre():
    pass

def list_games():
    pass

# Register the command
cli.add_command(add_game)

if __name__ == '__main__':
    cli()
