from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@34.105.183.54/m2m_db' # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 

class Products_ordered(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer)
    baskets = db.relationship('Baskets', backref='Products_ordered') 

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    baskets = db.relationship('Baskets', backref='Customers') 

class Baskets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products_ordered.product_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')