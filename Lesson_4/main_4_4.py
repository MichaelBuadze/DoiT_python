# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# string მოდულის გამოყენებით დაწერეთ შემოწმება.
# სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ ლათინურ ასოსა და
# მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით სიმბოლოებს: '!', '~', '#', '$' და ა.შ.


import string


txt = input("შეიყვანეთ სტრიქონი: ")

latin_letters = string.ascii_letters  # ლათინური ასოები
digits = string.digits  # ციფრები

ok_chars = latin_letters + digits

# შემოწმება
is_latin = False
for char in txt:
    if char in latin_letters:
        is_latin = True
        break  # თუ ვიპოვით ლათინურ ასოს, ვწყვეტთ და გადავდივართ შემდეგზე.

# შემოწმება
is_digit = False
for char in txt:
    if char in digits:
        is_digit = True
        break  # თუ ვიპოვით ციფრს, ვწყვეტთ და გადავდივართ შემდეგზე.

# შემოწმება
invalid_chars = False
for char in txt:
    if char not in ok_chars:
        invalid_chars = True
        break  # თუ ვიპოვით სიმბოლოს, ვწყვეტთ და გადავდივართ შედეგზე.

# ვალიდაციის შედეგი
if is_latin and is_digit and not invalid_chars:
    print("სტრიქონი ვალიდურია.")
else:
    print("სტრიქონი არ არის ვალიდური.") # ვალიდური არ არის "სფეისიც".