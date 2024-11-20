# გამოიცანი შემთხვევითი რიცხვი, შენ მიერ განსაზღვრულ დიაპაზონში

from random import randint
print("გამარჯობა, \nშენ, თავად უნდა გადაწყვიტო \n1-დან რამდენი რიცხვის ფარგლებში გსურს \nშემთხვევით შერჩეულის ამოცნობა.\n")
n = 0
while True:
    try:
        n = int(input("შეიყვანე ზღვარი: "))
        if not n or n < 0:
            raise ValueError
        break
    except ValueError:
        print("დაფიქსირდა შეცდობა! შეიყვანეთ დადებითი მთელი რიცხვი.")


print(f"შენი დიაპაზონია 1 - {n}")

# განსასაზღვრია ცდის რაოდენობა დიაპაზოების მიხედვით 


secret_number = randint(1, n)
i=1
print(f"\nგამოიცანი ჩაფიქრებული რიცხვი 1-დან {n}-მდე")
# ციკლი
while True:
    guess = int(eval(input(f"\nცდა ნომერი - {i} გამოიცანი რიცხვი: ")))
    
    if guess == secret_number:
        print(f"გილოცავთ! სწორად გამოიცანით. ეს არის {guess}")
        break
    elif guess > secret_number:
        print("ნაკლებია ჩანაფიქრი, კიდევ სცადე! ;)")
    else:
        print("ჩანაფიქრი უფრო მაღალია, სცადე უფრო დიდი რიცხვი!")
    i += 1
print("\nთამაში დასრულებულია!")       
