from flask import Flask, render_template
from models import Author, Book, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def books():
    books_list = Book.query.all()
    return render_template('books.html', books=books_list)

if __name__ == '__main__':
    app.run(debug=True)