from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# ✅ Define your Book model right here
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(100))
    genre = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    status = db.Column(db.String(50))

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        rating = request.form['rating']
        status = request.form['status']
        new_book = Book(title=title, author=author, genre=genre, rating=rating, status=status)
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')
    return render_template('add_book.html')
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.rating = request.form['rating']
        book.status = request.form['status']
        db.session.commit()
        return redirect('/')
    return render_template('edit_book.html', book=book)
@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
