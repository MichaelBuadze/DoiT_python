# მონაცემების შეყვანა კონსოლიდან
data = input("\nშეიყვანეთ მონაცემები გამოყოფილი სივრცეებით: ").split()
print()
# სიმრავლის შექმნა და დაბეჭდვა
unique_set = set(data)
print(unique_set)
print()
# frozenset-ის შექმნა
frozen_set = frozenset(unique_set)
print(frozen_set)
print()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
tuple_union = tuple(set1 | set2)
print(tuple_union)

# მონაცემების შეყვანა კონსოლიდან
data_tuple = tuple(map(int, input("\nშეიყვანეთ რიცხვები გამოყოფილი სივრცეებით: ").split()))
print()

# სიის შექმნა უნიკალური ელემენტებით
unique_list = list(set(data_tuple))
print(unique_list)
print()

data = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for name, age in data:
    print(f"Name: {name}, Age: {age}")

print()
users1 = ["Irakli", "Giorgi", "Nona", "Oto"]
users2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
print(users1)
print(users2)

print("\nდავბეჭდოთ მომხმარებლებს შორის დამთხვევა:\n")
common_users = set(users1) & set(users2)
print(common_users)