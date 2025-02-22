from sqlalchemy.orm import sessionmaker
from models import engine, Author, Book

Session = sessionmaker(bind=engine)
session = Session()



# =======> Insert Data <=======

# author1 = Author(name="Giorgi", book=[
#   Book(title="Book1"),
#   Book(title="Book2"),
#   Book(title="Book3"),
# ])

# session.add(author1)

# authors = [
#   Author(name="Paata", book=[
#     Book(title="Book4"),
#     Book(title="Book5"),
#   ]),
#   Author(name="Ana", book=[
#     Book(title="Book6"),
#     Book(title="Book7"),
#   ]),
#   Author(name="David", book=[
#     Book(title="Book8")
#   ]),
# ]

# session.add_all(authors)

# book9 = Book(title="Book9", author_id=1)

# session.add(book9)


# # ===============
# session.commit()

books = session.query(Book).all()

# print(books)

# for book in books:
#     print("-" * 35)
#     print(f"{book.id:<7}{book.title:<15}{book.author.name}")

# book = session.query(Book).filter_by(title = "book3").first()
# print(f"{book.id:<7}{book.title:<15}{book.author.name}")

# book_query = session.query(Book).filter_by(title = "book3")

# for book in book_query:
#     print(f"{book.id:<7}{book.title:<15}{book.author.name}")

authors = session.query(Author).all()
# for author in authors:
#     print("-" * 75)
#     # print(f"{author.id:<10}{author.name:<12}")
#     print(f"{author.id:<10}{author.name:<12}",
#           f"{[book.title for book in author.book]}")

for author in authors:
    print(f"{author.id:<5}{author.name:<12}", end = "")
    
    for book in author.book:
        print(f"{book.title:<7}", end = "")

    print()
# =======> Read Data <=======