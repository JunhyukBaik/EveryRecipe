from evr import db

class Cook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cook_name = db.Column(db.String(50), nullable=False)
    ingredient = db.Column(db.String(100), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)