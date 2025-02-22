from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, Table
from sqlalchemy.orm import declarative_base, relationship

# db = 'dialect[+driver]://username:password@host/database_name'
db = 'mysql+pymysql://openroot:openRoot2501@localhost:3307/lesson_30'

# engine = create_engine(db, echo=True)
engine = create_engine(db)

Base = declarative_base()



# =======> One to Many <=======

class Author(Base):
  __tablename__ = 'author'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)

  # ლოგიკური კავშირი – relationship – book ცხრილთან
  book = relationship('Book', back_populates='author')


class Book(Base):
  __tablename__ = 'book'

  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)

  author_id = Column(Integer, ForeignKey('author.id'))

  # ლოგიკური კავშირი – relationship – author ცხრილთან
  author = relationship('Author', back_populates='book')



# =======> One to One <=======

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, autoincrement=True)
  userName = Column(String(50), nullable=False, unique=True)
  email = Column(String(50), nullable=False)

  profile = relationship('Profile', back_populates='user', uselist=False)


class Profile(Base):
  __tablename__ = 'profile'

  id = Column(Integer, primary_key=True, autoincrement=True)
  bio = Column(Text)
  profilePicture = Column(String(200))
  user_userName = Column(String(50), ForeignKey("user.userName"))

  user = relationship('User', back_populates='profile')




# many to many


student_course_link = Table("student_course", Base.metadata,
                            Column("student_id", Integer, ForeignKey("student.id")),
                            Column("course_id", Integer, ForeignKey("course.id"))
                            )

class Student(Base):
  __tablename__ = 'student'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)

  course = relationship('Course', back_populates='student', secondary=student_course_link)


class Course(Base):
  __tablename__ = "course"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  
  student = relationship('Student', back_populates='course', secondary=student_course_link)








# ==============
if __name__ == '__main__':
  Base.metadata.create_all(engine)