import mysql.connector

# MySQL მონაცემთა ბაზასთან დაკავშირება
studentLlist_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Serfcxdrtgvc@2412",  # შეცვალეთ თქვენი პაროლით [ჩემი მაინც არ იმუშავებს სხვაგან :) ]
    port=3307,  # მე პორტის მითითებაც დამჭირდა, კარგად მაწვალა :) 
    database="student_db"  # აქაც ალბათ აჯობებს თქვენი კავშირის ბაზა გტამოიყენოთ. 
)

cursor = studentLlist_db.cursor()

# ცხრილის შექმნა
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    studentID INT AUTO_INCREMENT PRIMARY KEY,
    studentFirstName VARCHAR(50),
    studentLastName VARCHAR(50),
    studentAge INT
)
""")

# ცხრილში მონაცემების შეტანა
init_data = [
    ("გრიგოლ", "აბულაძე", 31),
    ("ანა", "გერგაული", 25),
    ("კოტე", "კახიძე", 27),
    ("ქეთევან", "კახიძე", 26),
    ("ანდრო", "შალიკაშვილი", 29)
]

cursor.executemany("INSERT INTO students (studentFirstName, studentLastName, studentAge) VALUES (%s, %s, %s)", init_data)
studentLlist_db.commit()

# მონაცემების ეკრანზე დაბეჭდვა
print("=" * 40)
print("დაწყებითი მონაცემები:")
print("=" * 40)
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)
    print("-" * 40)

# ახალი მონაცემის დამატება
new_data = ("ნინო", "ხარაზიშვილი", 24)
cursor.execute("INSERT INTO students (studentFirstName, studentLastName, studentAge) VALUES (%s, %s, %s)", new_data)
studentLlist_db.commit()

# მონაცემების ანბანური დალაგება (გვარი, სახელი)
cursor.execute("SELECT * FROM students ORDER BY studentLastName, studentFirstName")
sorted_data = cursor.fetchall()

# საბოლოო შედეგის დაბეჭდვა
print("=" * 40)
print("დალაგებული მონაცემები:")
print("=" * 40)
for row in sorted_data:
    print(row)
    print("-" * 40)

# კავშირის დახურვა
cursor.close()
studentLlist_db.close()
