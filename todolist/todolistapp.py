from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@34.105.183.54/todolist_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 

@app.route('/')
def home():
    return 'This is a to-do list!'

class todolist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable=False, default=False)
    status = db.Column(db.Boolean, nullable=False)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')