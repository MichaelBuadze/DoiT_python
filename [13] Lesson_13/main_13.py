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

import os
from fmain_13 import add_student, read_student_info, calculate_average_mark, update_student_mark, file_name

if os.path.exists(file_name):
    print("\nდამახსოვრებული სია:\n")
    # უკვე არსებული ინფორმაციის წაკითხვა
    read_student_info(file_name)
else:
    print("\nჯერჯერობით მონაცემთა ბაზა ცარიელია!\n")
# სტუდენტის დამატება
choice = ""
while choice != "არა":
    choice = input("\nგსურთ მორიგი მოსწავლის დამატება? \n\n - თუ გსურთ, დააჭირეთ Enter-ს \n - თუ არა, შეიყვანეთ 'არა': ")
    if choice != "არა":
        add_student(file_name)
    else:
       continue

# თუ შეყვანილ იქნა 'არა' და ამ დროს ფაილი არც კი შექმნილა, 
# გაჩერდება პროგრამა და გამოიტანს შეტყობინებას - 'ფაილი არ შექმნილა' 
# ... სხვა შემთხვევაში პროგრამა გაგრძელდება
if not os.path.exists(file_name):
    print("\nფაილი არ შექმნილა.")
else:
    print("\nმიმდინარე რეაგირების შედეგი:\n")
    # ინფორმაციის წაკითხვა
    read_student_info(file_name)
    
    # კონკრეტული სტუდენტის ინფორმაციის წაკითხვა
    enter_student_id = input("\nსასურველი სტუდენტის ინფორმაციის გამოსატანად შეიყვანეთ მისი ID: ")
    read_student_info(file_name, student_id=enter_student_id)
        
    # საშუალო ქულების გამოთვლა
    print("\nსაგნების საშუალო ქულები:\n")
    calculate_average_mark(file_name)

    # სტუდენტის ქულის განახლება
    renew_student_id = input("\nშეიყვანეთ გასაახლებელი სტუდენტის ID: ")
    print() # თავისუფალი სივრცე
    renew_student_subject = input("\nშეიყვანეთ გასაახლებელი სტუდენტის საგანი: ")
    print() # თავისუფალი სივრცე
    update_student_mark(file_name, student_id=renew_student_id, subject_name=renew_student_subject, new_mark=85.5)
    print() # თავისუფალი სივრცე
    read_student_info(file_name, student_id=renew_student_id)
