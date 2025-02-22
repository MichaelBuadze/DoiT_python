from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


# მოხერხებულობისთვის აქვე კომენტარებად განთავსდა ოპერაციული კოდები:

# flask db init
# flask db migrate -m "Initial migration"
# flask db upgrade

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    return redirect(url_for('create_book'))  # მთავარი გვერდი გადამისამართდება /book-ზე

@app.route('/book', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        new_book = Book(title=title, author=author, year=year)
        db.session.add(new_book)
        db.session.commit()
        return redirect('/books')

    return render_template('create_book.html')

@app.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = request.form['year']
        db.session.commit()
        return redirect('/books')
    return render_template('create_book.html', book=book)

@app.route('/get_book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year})

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return render_template('books.html', books=books)  # ახალი HTML გვერდი ყველა წიგნის სიისთვის

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'წიგნი წარმატებით წაიშალა'})



# =============================

if __name__ == '__main__':
    app.run(debug=True)
