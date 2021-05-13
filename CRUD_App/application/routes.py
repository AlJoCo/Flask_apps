from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/')
@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete/<name>')
def delete(name):
    condemned_game = Games.query.first() #if no entry is given, the first entry is deleted (less than ideal)
    condemned_game.name = name
    db.session.delete(condemned_game)
    db.session.commit()
    return "Game deleted"

@app.route('/count')
def count():
    game_count = Games.query.count()
    return (f'There are {game_count} games on record')