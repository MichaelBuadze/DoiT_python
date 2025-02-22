from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# db = "dialect[+driver]://uesrname"password@host/database_name"
db = "mysql+pymysql://root:Serfcxdrtgvc%402412@localhost:3307/lesson_30"

engine = create_engine(db, echo=False)

Base = declarative_base()

# ===============>  One to Many <===============

class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(50), nullable = False)

     # ლოგიკური კავშირი relationship - book ცხრილიდან

    book = relationship ("Book", back_populates = "author" )

class Book(Base):
    __tablename__ = "book"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(50), nullable = False)

    author_id = Column(Integer, ForeignKey("author.id"))

    # ლოგიკური კავშირი relationship - author ცხრილიდან

    author = relationship ("Author", back_populates = "book" )


# ================================================================

if __name__ == "__main__":
    Base.metadata.create_all(engine)