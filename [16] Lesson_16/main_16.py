from fmain_16 import Car, ElectricCar
from car_data import car_data

# მონაცემების იმპორტი car_data.py-დან
cars = []
for data in car_data:
    if "battery_life" in data:
        car = ElectricCar(data["brand"], data["model"], data["year"], data["battery_life"])
    else:
        car = Car(data["brand"], data["model"], data["year"])
    cars.append(car)

# სათაურის ზოლის და არსებული მანქანების ინფორმაციის გამოტანა
print("=" * 70)
print(f"{'ბრენდი':<15} {'მოდელი':<10} {'გამოშვება':<10} {'ასაკი':<10} {'ტიპი':<13} {'ელემენტი':<10}")
print("=" * 70)
for car in cars:
    car.car_info()
    print("-" * 70)
# კონსოლიდან ახალი მანქანების შეყვანა
while True:
    brand = input("\nშეიყვანეთ მანქანის ბრენდი ან შეიყვანეთ 'არა' რათა შეწყვიტოთ: ")
    if brand == "არა" or brand.lower() == "ara":
        break

    model = input("შეიყვანეთ მანქანის მოდელი: ")
    year = int(input("შეიყვანეთ გამოშვების წელი: "))

    car_type = input("ეს ელექტრო მანქანაა? (დიახ/არა): ").strip().lower()
    
    if car_type == "დიახ":
        battery_life = int(input("შეიყვანეთ ბატარეის ხანგრძლივობა საათებში: "))
        new_car = ElectricCar(brand, model, year, battery_life)
    else:
        new_car = Car(brand, model, year)

    cars.append(new_car)
    print("\nახალი მანქანის დამატება წარმატებით შესრულდა:")
    print("=" * 70)
    print(f"{'ბრენდი':<15} {'მოდელი':<10} {'გამოშვება':<10} {'ასაკი':<10} {'ტიპი':<13} {'ელემენტი':<10}")
    print("=" * 70)
    new_car.car_info()

print("=" * 70)
print(f"{'ბრენდი':<15} {'მოდელი':<10} {'გამოშვება':<10} {'ასაკი':<10} {'ტიპი':<13} {'ელემენტი':<10}")
print("=" * 70)
for car in cars:
    car.car_info()
    print("-" * 70)

# მანქანების საერთო რაოდენობის ჩვენება
Car.total_cars()
