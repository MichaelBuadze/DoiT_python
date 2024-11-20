import json
import os


# მისამართის კლასი
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


# სტუდენტის კლასი
class Student:
    row_id = 0

    def __init__(self, name, mark, address):
        Student.row_id += 1
        self.row_id = Student.row_id
        self.name = name
        self.mark = mark
        self.address = address
        self.grade = self.calculate_grade(mark)

    @staticmethod
    def calculate_grade(mark):
        if mark >= 91:
            return "A"
        elif mark >= 81:
            return "B"
        elif mark >= 71:
            return "C"
        else:
            return "D"


# ფაილის წაკითხვა არსებული მონაცემების ჩასატვირთად
def load_students_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# კონსოლიდან ახალი სტუდენტების შეყვანა
def input_students():
    students = []

    while True:
        cont = input("გსურთ სხვა სტუდენტის დამატება? (დიახ/არა): ").strip().lower()
        if cont not in ("დიახ", "კი", "ki", "diax", "ok"):
            break
        name = input("შეიყვანეთ სტუდენტის სახელი: ").strip()
        if not name:
            print("სახელი სავალდებულოა!")
            continue

        try:
            mark = int(input("შეიყვანეთ სტუდენტის ქულა (0-100): ").strip())
            if not (0 <= mark <= 100):
                raise ValueError
        except ValueError:
            print("ქულა უნდა იყოს მთელი რიცხვი, 0-დან 100-მდე!")
            continue
        while True:    
            city = input("შეიყვანეთ ქალაქი: ").strip()
            if not city:
                print("ქალაქი სავალდებულოა!")
                continue
            else:
                break

        street = input("შეიყვანეთ ქუჩა: ").strip()
        if not street:
            print("ქუჩა სავალდებულოა!")
            continue

        address = Address(city, street)
        student = Student(name, mark, address)
        students.append(student)

        # cont = input("გსურთ სხვა სტუდენტის დამატება? (დიახ/არა): ").strip().lower()
        # if cont not in ("დიახ", "კი"):
        #     break

    return students


# ძირითადი პროგრამა
FILENAME = "students.json"

# ფაილიდან არსებული სტუდენტების მონაცემების ჩატვირთვა
existing_students = load_students_from_file(FILENAME)

# ფაილის ცარიელობის შემოწმება
if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
    
    # თუ ფაილი არ არის ცარიელი, არ დავამატოთ default_students
    default_students = []
else:
    default_students = [
    Student("Paata", 87, Address("Tbilisi", "Saburtalo")),
    Student("Demetre", 100, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Alexander", 100, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Teona", 92, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Nino", 99, Address("Tbilisi", "Leselidzs str. 25")),
    Student("Andria", 87, Address("Tbilisi", "Varketili IV 407-5-123")),
]
# Student.row_id-ის განახლება
Student.row_id = max(
    (student.get("row_id", 0) for student in existing_students), default=0
)

# კონსოლიდან ახალი სტუდენტების შეყვანა
new_students = input_students()

# არსებული, შაბლონური და ახალი სტუდენტების გაერთიანება
all_students = (
    existing_students
    + [
        {
            "row_id": student.row_id,
            "name": student.name,
            "mark": student.mark,
            "address": {"city": student.address.city, "street": student.address.street},
            "grade": student.grade, 

        }
        for student in default_students + new_students
    ]
)

# მონაცემების ფაილში შენახვა
with open(FILENAME, "w", encoding="utf-8") as file:
    json.dump(all_students, file, ensure_ascii=False, indent=2)

print("\nმონაცემები წარმატებით შეინახა ფაილში!")