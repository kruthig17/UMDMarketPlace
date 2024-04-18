from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
# db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SECRET_KEY'] = 'secretkey'


"""class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(60), nullable = False)
"""
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/orderhistory')
def orderhistory():
    return render_template('orderhistory/orderhistory.html')

@app.route('/shopping')
def shop():
    items = [
    {"name": "Item 1", "description": "Description for Item 1","price":"$250", "image": "https://via.placeholder.com/150"},
    {"name": "Item 2", "description": "Description for Item 2", "image": "https://via.placeholder.com/150","price":"$350"},
    {"name": "Item 3", "description": "Description for Item 3", "image": "https://via.placeholder.com/150","price":"$250"},
    {"name": "Item 4", "description": "Description for Item 4", "image": "https://via.placeholder.com/150","price":"$150"},
    {"name": "Item 5", "description": "Description for Item 5", "image": "https://via.placeholder.com/150","price":"$50"}
]


    return render_template('shop/shop.html', items=items)
if __name__ == '__main__':
    app.run(debug=True)
