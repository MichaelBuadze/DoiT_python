# დაწერეთ პროგრამა, რომელიც ტერმინალში მომხმარებელს გამოუტანს სტუდენტების აიდის (id) სიას, 
# მომხარებელი აირჩევს სტუდენტის აიდის, 
# მიიღებული აიდისთვის დაბეჭდავს სტუდენტის მონაცემებს. 
# მონაცემებში უნდა დაიბეჭდოს:
# (სახელი, გვარი, ასაკი და ქულა თითოეული საგნის მიხედვით)



# მონაცემების ლექსიკონი
my_dict = {
    "students": [
        {"id": 20, "name": "Giorgi", "age": 25},
        {"id": 25, "name": "Giorgi", "age": 23},
        {"id": 100, "name": "Nika", "age": 22},
        {"id": 56, "name": "Nika", "age": 25},
        {"id": 1232, "name": "Dato", "age": 22},
        {"id": 846723, "name": "Archili", "age": 32}
    ],
    "subjects": [
        {"name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
        {"name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
        {"name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
        {"name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
        {"name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}}
    ]
}

#სტუდენტების ID-ების, სიდიდის მიხედვით სორტირება მის გამოტანამდე
sorted_ID = sorted(my_dict["students"], key=lambda x: x["id"])

# სტუდენტების ID-ების გამოტანა
print("\nსტუდენტების ID:\n")
# for student in my_dict["students"]:
#     print(student["id"], end="; ")
for student in sorted_ID:
    print(student["id"], end="; ")
print()  # ახალი ცარიელი ხაზის დამატება

# სტუდენტის ID-ის არჩევა (შეგვყავს ID რიცხვი)
selected_id = input("\nაირჩიეთ სტუდენტის ID: ")

# სტუდენტი ID-ის მიხედვით:
selected_student = None
for student in my_dict["students"]:
    if str(student["id"]) == selected_id:
        selected_student = student
        break

# თუ სტუდენტი მოიძებნა
if selected_student:
    print(f"\nსტუდენტი: {selected_student['name']}, {selected_student['age']} წლის;")

    # საგნების სორტირება სახელების მიხედვით
    sorted_subjects = sorted(my_dict["subjects"], key=lambda x: x["name"])

    # თითოეული საგნის შეფასების გამოტანა
    print("\nშეფასება საგნების მიხედვით:\n")
    for subject in sorted_subjects:
        grade = subject["grades"].get(selected_id, "არ შეფასებულა")
        print(f"{subject['name']:<10} - {grade}")
else:
    print("სტუდენტი ამ ID-ით ვერ მოიძებნა!")
