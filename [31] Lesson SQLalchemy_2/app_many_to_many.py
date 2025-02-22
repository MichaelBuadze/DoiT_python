from sqlalchemy.orm import sessionmaker
from models import engine, Student, Course, student_course_link

Session = sessionmaker(bind=engine)
session = Session()


# insert data


python = Course(name="PYTHON")
java = Course(name="Java")
html_css = Course(name="HTML/CSS")

vaja = Student(name="Vaja", course=[python, html_css])
gela = Student(name="Gela", course=[java, html_css])
lela = Student(name="Lela", course=[python, java])



# session.add_all([python, java, html_css, vaja, gela, lela])
# session.commit()




#  read data


# students = session.query(Student).all()


# for student in students:
#     # print(student.id, student.name, student.course[1].name)

#      print(student.id, student.name, [course.name for course in student.course])

students = session.query(Student).all()

for student in students:
    for course in student.course:
        if course.name == "PYTHON":
             print(student.id, student.name, [course.name for course in student.course])


    
