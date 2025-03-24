from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(100))
    genre = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    status = db.Column(db.String(50))
