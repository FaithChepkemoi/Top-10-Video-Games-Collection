# Top-10-Video-Games-Collection
The Top 10 Video Games Collection is a CLI-based application that allows users to create and manage their own ranked list of favorite video games. Users can add, edit, delete, sort, rank, and search for games in their collection. The application ensures data persistence by storing game information in a database using an ORM.

## Features

- Add a Game – Users can enter a new game into their top 10 list.
- Edit a Game – Modify details of a game (title, genre, platform, release year, rating).
- Delete a Game – Remove a game from the list.
- View All Games – Display the list of top 10 games with their details.
- Rank Games – Assign ranks (1-10) to each game based on preference.
- Sort Games – Sort the list by title, release year, rating, or genre.
- Search for a Game – Look up a game by name.

## Installation

 ### Prerequisites

- Python 3.x
- pipenv (for virtual environment and dependency management)
- SQLite (built-in with Python, but required for ORM functionality)
- SQLAlchemy (for ORM database management)
- Click (for building the CLI interface)

## Steps to Install

1. *Clone the Repository*:
~~~bash
git clone https://github.com/FaithChepkemoi/Top-10-Video-Games-Collection
~~~

2. *Create a virtual environment and install dependencies* :
~~~bash
pip install pipenv 
pipenv install
pipenv shell
~~~

3. *Install necessary Python packages:*:
~~~bash
pipenv install sqlalchemy
pipenv install click  # For CLI handling
~~~

4. *Set up the database*:
~~~bash
python lib/models/init_db.py
~~~
5. *Run the application*:
~~~bash
python lib/cli.py
~~~

## Usage
Once the program is running, use the following commands to run:
 1. *Add the game*:
   ~~~bash
    python3 main.py add-game
~~~
 2. *Add game details*:
   ~~~bash
    python3 main.py add-game-deatils
~~~
 3. *View the  games avialable*:
   ~~~bash
    python3 main.py list-games
~~~
 4. *edit game*:
   ~~~bash
    python3 main.py edit-game
~~~

 5. *Rank the game*:
   ~~~bash
    python3 main.py rank-game
~~~

 6. *Sort games*:
   ~~~bash
    python3 main.py sort-games
~~~

## Contributing

If you’d like to contribute to this project:

- Fork the repository
- Create a new branch 
   ~~~bash
    git checkout -b feature-branch
~~~

- Commit your changes 
   ~~~bash
   git commit -m "Added new feature"
~~~

- Push to the branch 
   ~~~bash
    git push origin feature-branch
~~~

- Create a Pull Request

## License

This project is open-source and available under the MIT License.

