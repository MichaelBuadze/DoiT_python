import threading

# ლუწი რიცხვების ძაფი (ლუწი რიცხვების გამორჩევის პროცესი)
def find_even_numbers():
    even_numbers = [num for num in range(n_start, n_end) if num % 2 == 0]
    print("ლუწი რიცხვები:", even_numbers)

# კენტი რიცხვების ძაფი (კენტი რიცხვების გამორჩევის პროცესი)
def find_odd_numbers():
    odd_numbers = [num for num in range(n_start, n_end) if num % 2 != 0]
    print("კენტი რიცხვები:", odd_numbers)

# ძირითადი პროგრამის სათაური და მომზადება სრული პროცესისთვის
print("=" * 60) # დეკორაციული ელემენტი
print("კენტი და ლუწი რიცხვების მაძიებელი პროგრამა.")
print("=" * 60) # დეკორაციული ელემენტი
print() # თავისუფალი სოვრცე
n_start = int(input("დიაპაზონის საწისი: "))
n_end = int(input("დიაპაზონის სასრული: "))
print() # თავისუფალი სოვრცე
print("/" * 60) # დეკორაციული ელემენტი
print() # თავისუფალი სოვრცე


# ძაფების (პროცესების) შექმნა
even_thread = threading.Thread(target=find_even_numbers)
odd_thread = threading.Thread(target=find_odd_numbers)

# ძაფების (პროცესების) თანადროული გაშვება
even_thread.start()
print("-" * 60) # დეკორაციული ელემენტი
odd_thread.start()
print("-" * 60) # დეკორაციული ელემენტი

# ველოდებით ძაფების დასრულებას
even_thread.join()
odd_thread.join()

print("რიცხვების ძიება დასრულდა.")
