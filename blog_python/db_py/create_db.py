from flask import Flask
from models import Author, Book, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        author1 = Author(name='Жюль Верн', birth_year=1828, country='Франция')
        author2 = Author(name='Джордж Оруэлл', birth_year=1903, country='Великобритания')
        author3 = Author(name='Рэй Брэдбери', birth_year=1920, country='США')
        author4 = Author(name='Джон Уиндем', birth_year=1903, country='Великобритания')
        author5 = Author(name='Станислав Лем', birth_year=1921, country='Польша')
        author6 = Author(name='Гарри Гаррисон', birth_year=1925, country='США')
        author7 = Author(name='Уильям Гибсон', birth_year=1948, country='США')

        db.session.add_all([author1, author2, author3, author4, author5, author6, author7])
        db.session.commit()

        book1 = Book(title='Вокруг света за 80 дней', year=1872, genre='Приключения', pages=320, author=author1)
        book2 = Book(title='1984', year=1949, genre='Антиутопия', pages=328, author=author2)
        book3 = Book(title='Марсианские хроники', year=1950, genre='Научная фантастика', pages=222, author=author3)
        book4 = Book(title='День триффидов', year=1951, genre='Постапокалипсис', pages=304, author=author4)
        book5 = Book(title='Солярис', year=1961, genre='Научная фантастика', pages=204, author=author5)
        book6 = Book(title='Стальная крыса', year=1957, genre='Космическая опера', pages=256, author=author6)
        book7 = Book(title='Нейромант', year=1984, genre='Киберпанк', pages=320, author=author7)

        db.session.add_all([book1, book2, book3, book4, book5, book6, book7])
        db.session.commit()