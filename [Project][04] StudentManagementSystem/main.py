import json
import os


# სტუდენტის კლასი, რომელიც ინახავს სტუდენტის მონაცემებს
class Student:
    def __init__(self, student_id: int, name: str, grade: str):
        self.student_id = student_id  # უნიკალური ID
        self.name = name  # სტუდენტის სახელი
        self.grade = grade  # შეფასება

    def update_grade(self, new_grade: str):
        self.grade = new_grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade,
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["grade"],
        )


class StudentManagementSystem:
    # ფაილის სახელის განსაზღვრა სკრიპტის დირექტორიაში
    FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")

    def __init__(self):
        self.students = []
        self.load_data()

    # მონაცემების ჩატვირთვა JSON ფაილიდან
    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.students = [Student.from_dict(student) for student in data]

    # მონაცემების შენახვა JSON ფაილში
    def save_data(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in self.students], file, ensure_ascii=False, indent=4)

    # სიის ნომრების გადანომრება
    def renumber_roll_numbers(self):
        for index, student in enumerate(self.students, start=1):
            student.roll_number = index

    # ახალი სტუდენტის დამატება
    def add_student(self, name: str, grade: str):
        if not grade.isalpha() or len(grade) != 1:
            print("ინფორმაცია არასწორია. შეფასება უნდა იყოს ერთი ასო.")
            return
        new_id = max((student.student_id for student in self.students), default=0) + 1
        new_student = Student(new_id, name, len(self.students) + 1, grade)
        self.students.append(new_student)
        self.save_data()
        print("სტუდენტი წარმატებით დაემატა.")

    # ყველა სტუდენტის ნახვა
    def view_all_students(self):
        if not self.students:
            print("სტუდენტი ვერ მოიძებნა, სია ცარიელია.")
            return
        print("=" * 65)
        print(f" {'სტუდენტის ID':<20} {'სრული სახელი':<20} {'შეფასება':<20} ")
        print("=" * 65)
        for student in self.students:
            print(
                f" {student.student_id:<20} {student.name:<20} {student.grade:<20} "
            )
            print("-" * 65)

    # სტუდენტის ძებნა ID-ის მიხედვით
    def search_student_by_id(self, student_id: int):
        for student in self.students:
            if student.student_id == student_id:
                print("=" * 65)
                print(f" {'სტუდენტის ID':<20} {'სრული სახელი':<20} {'შეფასება':<20} ")
                print("=" * 65)
                print(f" {student.student_id:<20} {student.name:<20} {student.grade:<20}")
                print("-" * 65)
                return
        print(f"სტუდენტი ID {student_id} ვერ მოიძებნა.")

    # სტუდენტის წაშლა ID-ის მიხედვით
    def delete_student(self, student_id: int):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_data()
                print("სტუდენტი წარმატებით წაიშალა.")
                return
        print(f"სტუდენტი ID {student_id} ვერ მოიძებნა.")

    # სტუდენტის შეფასების განახლება
    def update_student_grade(self, student_id: int, new_grade: str):
        for student in self.students:
            if student.student_id == student_id:
                student.update_grade(new_grade)
                self.save_data()
                print("შეფასება წარმატებით განახლდა.")
                return
        print(f"სტუდენტი ID {student_id} ვერ მოიძებნა.")

    # პროგრამის მენიუს ფუნქციონალი
    def run(self):
        while True:
            print("\nსტუდენტების მართვის სისტემის მენიუ:\n")
            print("1. ყველა სტუდენტის ნახვა")
            print("-" * 30)
            print("2. ახალი სტუდენტის დამატება")
            print("-" * 30)
            print("3. სტუდენტის ძებნა ID-ით")
            print("-" * 30)
            print("4. სტუდენტის შეფასების განახლება")
            print("-" * 30)
            print("5. სტუდენტის წაშლა ID-ით")
            print("-" * 30)
            print("6. გასვლა\n")

            choice = input("აირჩიეთ მოქმედება: ")
            if choice == '1':
                self.view_all_students()
            elif choice == '2':
                while True:
                    name = input("შეიყვანეთ სტუდენტის სახელი: ")
                    if not name:
                        print("სახელი აუცილებელი ველია, გთხოვთ შეიყვანოთ სახელი!")
                    elif name.isdigit():
                        print("დაფიქსირდა შეცდომა, შეიყვანეთ სახელი სწორად!")
                        continue
                    else:
                        break
                grade = input("შეიყვანეთ შეფასება: ")
                self.add_student(name, grade)
            elif choice == '3':
                try:
                    student_id = int(input("შეიყვანეთ სტუდენტის ID: "))
                except ValueError:
                    print("ID უნდა იყოს რიცხვი.")
                    continue
                self.search_student_by_id(student_id)
            elif choice == '4':
                try:
                    student_id = int(input("შეიყვანეთ სტუდენტის ID: "))
                except ValueError:
                    print("ID უნდა იყოს რიცხვი.")
                    continue
                new_grade = input("შეიყვანეთ ახალი შეფასება: ")
                if not new_grade.isalpha() or len(new_grade) != 1:
                    print("შეფასება უნდა იყოს ერთი ასო.")
                    continue
                self.update_student_grade(student_id, new_grade)
            elif choice == '5':
                try:
                    student_id = int(input("შეიყვანეთ სტუდენტის ID: "))
                except ValueError:
                    print("ID უნდა იყოს რიცხვი.")
                    continue
                self.delete_student(student_id)
            elif choice == '6':
                print("პროგრამის დასრულება.")
                break
            else:
                print("არასწორი არჩევანი. სცადეთ ხელახლა.")


if __name__ == "__main__":
    print("="*75)
    print("ს ტ უ დ ე ნ ტ ე ბ ი ს   მ ა რ თ ვ ი ს   ს ი ს ტ ე მ ა")
    print("="*75)
    sms = StudentManagementSystem()
    sms.run()
