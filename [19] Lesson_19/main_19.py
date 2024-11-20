import json


# მისამართის კლასი
class Address:
    def __init__(self, city, street):
        """
        ინიციალიზაცია Address კლასისთვის
        პარამეტრი city: ქალაქი
        პარამეტრი street: ქუჩა
        """
        self.city = city
        self.street = street


# სტუდენტის კლასი
class Student:
    # სტატიკური ატრიბუტი უნიკალური იდენტიფიკატორისთვის
    row_id = 0

    def __init__(self, name, mark, address):
        """
        ინიციალიზაცია Student კლასისთვის
        პარამეტრი name: სტუდენტის სახელი
        პარამეტრი mark: ქულა
        პარამეტრი address: მისამართი (Address კლასის ობიექტი)
        """
        Student.row_id += 1
        self.row_id = Student.row_id
        self.name = name
        self.mark = mark
        self.address = address


# სტუდენტების სია
students = [
    Student("Paata", 87, Address("Tbilisi", "Saburtalo")),
    Student("Demetre", 100, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Alexander", 100, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Teona", 92, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Nino", 99, Address("Tbilisi", "Leselidzs str. 25")),
    Student("Andria", 87, Address("Tbilisi", "Varketili IV 407-5-123")),
]

# სტუდენტების json ფორმატში გადაყვანა
students_data = [
    {
        "row_id": student.row_id,
        "name": student.name,
        "mark": student.mark,
        "address": {"city": student.address.city, "street": student.address.street},
    }
    for student in students
]

# მონაცემების ფაილში შენახვა
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students_data, file, ensure_ascii=False, indent=2)

# ფაილის წაკითხვა
with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

# ცვლილებები მონაცემებზე
for student in loaded_students:
    # ქულის მიხედვით grade-ის დამატება
    mark = student["mark"]
    if mark >= 91:
        student["grade"] = "A"
    elif mark >= 81:
        student["grade"] = "B"
    elif mark >= 71:
        student["grade"] = "C"
    else:
        student["grade"] = "D"

# შეცვლილი მონაცემების ფაილში შენახვა
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(loaded_students, file, ensure_ascii=False, indent=2)


