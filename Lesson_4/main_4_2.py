#2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# ჩამოაშორეთ ზედმეტი ინტერვალები.
# ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
# დაუმატეთ ქვესტრიქონი 'Python'.
# თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

# მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია `.strip()`.

# მაგ.: "  Python is funny     ".strip()   ====>  "Python is funny"

txt = input("შეიყვანეთ ტექსტი: ")
txt = txt.strip().lower()

if "python" in txt:
    txt = txt.replace("python", "Python")
else:
    txt += " Python"

print(txt)