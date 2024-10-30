# შექმენით csv  ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,mark
# 1,string,0,string,string,0
# 2,string,0,string,string,0

# 1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი შეიყვანს ინფორმაციას(id,name,age,grade,subject_name,mark) 
#    და თქვენ სტუდენტს დაამატებს csv ფაილში. დაასორტირეთ მონაცემები id-ის მიხედვით.
# 2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, 
#    ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.
# 3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (marks) საგნების მიხედვით.
# 4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. 
#    მომხარებელი შეიყვანს სტუდენტის id, საგანს და განახლებულ ქულას.

import csv
import os

# CSV დიალექტის რეგისტრაცია
csv.register_dialect('dialect', delimiter='|', quoting=csv.QUOTE_NONNUMERIC)

# ფუნქცია, რომელიც ამოწმებს ფაილის არსებობას და სათაურს ამატებს თუ არ არსებობს
def initialize_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['ID', 'სახელი', 'ასაკი', 'კლასი', 'საგანი', 'ქულა']
            writer = csv.DictWriter(file, fieldnames=fieldnames, dialect='dialect')
            writer.writeheader()  # სათაურის ჩაწერა

# ფუნქცია, რომელიც მომხმარებელს აძლევს საშუალებას დაამატოს ახალი სტუდენტი csv ფაილში.
def add_student(file_name):
    # ფაილის ინიციალიზაცია სათაურით
    initialize_file(file_name)

    # მომხმარებლისგან ID-ის შეყვანა და შემოწმება არსებობს თუ არა ბაზაში
    while True:
        student_id = input("\nშეიყვანეთ სტუდენტის ID: ")
        if not check_id_exists(file_name, student_id):
            break  # თუ ID არ არსებობს, ვწყვეტთ ციკლს და ვაგრძელებთ მონაცემების შეყვანას
        print("შეყვანილი ID უკვე არსებობს ბაზაში, სცადეთ სხვა ID.")

    # სხვა მონაცემების შეყვანა
    name = input("შეიყვანეთ სტუდენტის სახელი: ")

    # ასაკის ვალიდაცია
    while True:
        age_input = input("შეიყვანეთ ასაკი: ")
        if age_input.isdigit():  # თუ ასაკი რიცხვია
            age = int(age_input)
            break
        else:
            print("ასაკი უნდა იყოს რიცხვი, სცადეთ თავიდან.")

    grade = input("შეიყვანეთ კლასი: ")
    subject_name = input("შეიყვანეთ საგანი: ")
    
    # ქულის ვალიდაცია
    while True:
        try:
            mark = float(input("შეიყვანეთ ქულა: "))
            break
        except ValueError:
            print("ქულა უნდა იყოს რიცხვითი ფორმატით. სცადეთ თავიდან.")

    # მონაცემების ჩაწერა csv ფაილში
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['ID', 'სახელი', 'ასაკი', 'კლასი', 'საგანი', 'ქულა']
        writer = csv.DictWriter(file, fieldnames=fieldnames, dialect='dialect')
        writer.writerow({
            'ID': student_id,
            'სახელი': name,
            'ასაკი': age,
            'კლასი': grade,
            'საგანი': subject_name,
            'ქულა': mark
        })

    # მონაცემების დასორტირება ID-ის მიხედვით
    sort_csv_by_id(file_name)

# ფუნქცია, რომელიც ამოწმებს, არსებობს თუ არა ID csv ფაილში
def check_id_exists(file_name, student_id):
    if os.path.exists(file_name):
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, dialect='dialect')
            for row in reader:
                if row['ID'] == student_id:
                    return True
    return False

# ფუნქცია, რომელიც სორტირებს csv ფაილს ID-ის მიხედვით
def sort_csv_by_id(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, dialect='dialect')
        header = reader.fieldnames
        sorted_data = sorted(reader, key=lambda x: int(x['ID']))

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header, dialect='dialect')
        writer.writeheader()
        writer.writerows(sorted_data)

# ფუნქცია, რომელიც კითხულობს ყველა ან კონკრეტული სტუდენტის მონაცემებს
def read_student_info(file_name, student_id=None):
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, dialect='dialect')
        w1 = 10
        w2 = 20
        count = 0
        lines = 78
        print('=' * lines)
        for row in reader:
            if student_id is None or row['ID'] == str(student_id):
                if count == 0:
                    head = tuple(row.keys())
                    print(f"  {head[0]:<{w1}}{head[1]:<{w2}}{head[2]:<{w1}}{head[3]:<{w1}}{head[4]:<{w2}}{head[5]}")
                    print('=' * lines)

                    count += 1
                print(f"  {row['ID']:<{w1}}{row['სახელი']:<{w2}}{row['ასაკი']:<{w1}}{row['კლასი']:<{w1}}{row['საგანი']:<{w2}}{row['ქულა']}")

                print('-' * lines)

# ფუნქცია, რომელიც ითვლის საგნების საშუალო ქულას
def calculate_average_mark(file_name):
    marks = {}
    counts = {}

    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, dialect='dialect')
        for row in reader:
            subject = row['საგანი']
            mark = float(row['ქულა'])

            if subject in marks:
                marks[subject] += mark
                counts[subject] += 1
            else:
                marks[subject] = mark
                counts[subject] = 1
    w2 = 20
    lines = 78
    for subject, total_marks in marks.items():
        average = total_marks / counts[subject]
        print('-' * lines)
        print(f"{subject}-ის საშუალო ქულა არის: {average:.2f}")

# ფუნქცია, რომელიც ანახლებს სტუდენტის ქულას კონკრეტულ საგანში
def update_student_mark(file_name, student_id, subject_name, new_mark):
    rows = []
    updated = False

    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, dialect='dialect')
        header = reader.fieldnames
        for row in reader:
            if row['ID'] == str(student_id) and row['საგანი'] == subject_name:
                row['ქულა'] = str(new_mark)
                updated = True
            rows.append(row)

    if updated:
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header, dialect='dialect')
            writer.writeheader()
            writer.writerows(rows)
        print("ქულა განახლებულია.")
    else:
        print("ჩანაწერი ვერ მოიძებნა.")


# csv ფაილის სახელი
file_name = '[13] Lesson_13/students.csv'

# სტუდენტის დამატება
choice = ""
while choice != "არა":
    choice = input("\n გსურთ მორიგი მოსწავლის დამატება? \n - თუ გსურთ, დააჭირეთ Enter-ს \n - თუ არა, შეიყცენეთ - არა    - ")
    if choice != "არა":
        add_student(file_name)
    else:
       continue

# თუ შეყვანილ იქნა "არა" და ამ დროს ფაილი არც კი შექმნილა, გაჩერდება პროგრამა და გამოიტანს შეტყობინებას - ფაილი არ შექმნილა 
# ... სხვა შემთხვევაში პროგრამა გაგრძელდება
if not os.path.exists(file_name):
    print("\nფაილი არ შექმნილა.")
else:     

    print() # თავისუფალი სივრცე

    # ყველა სტუდენტის ინფორმაციის წაკითხვა
    read_student_info(file_name)

    print() # თავისუფალი სივრცე

    # კონკრეტული სტუდენტის ინფორმაციის წაკითხვა
    enter_student_id = input("შეიყვანეთ სასურველი სტუდენტის ID: ")
    print() # თავისუფალი სივრცე
    read_student_info(file_name, student_id=enter_student_id)

    print() # თავისუფალი სივრცე

    # საშუალო ქულების გამოთვლა
    calculate_average_mark(file_name)

    print() # თავისუფალი სივრცე

    # სტუდენტის ქულის განახლება
    renew_student_id = input("შეიყვანეთ გასაახლებელი სტუდენტის ID: ")
    print() # თავისუფალი სივრცე
    renew_student_subject = input("შეიყვანეთ გასაახლებელი სტუდენტის საგანი: ")
    print() # თავისუფალი სივრცე
    update_student_mark(file_name, student_id=renew_student_id, subject_name=renew_student_subject, new_mark=85.5)
    print() # თავისუფალი სივრცე
    read_student_info(file_name, student_id=renew_student_id)