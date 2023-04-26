from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/royw/Documents/projects/recipes-api/database.db'

db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    desicrption = db.Column(db.String(80))

@app.route('/user', methods=['GET'])
def get_all_user():
    return ''

@app.route('/user/<user_id>', methods=['GET'])
def get_one_user():
    return ''

@app.route('/user', methods=['POST'])
def create_user():
    return ''

@app.route('/user/<user_id>', methods=['PUT'])
def promote_user():
    return ''

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user():
    return '' 


if __name__ == '__main__':
    app.run(debug=True)