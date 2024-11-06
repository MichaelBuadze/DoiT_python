from datetime import datetime

class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def car_info(self):
        car_type = "ჩვეულებრივი"
        battery_info = ""
        print(f"{self.brand:<15} {self.model:<10} {self.year:<12} {self.age_of_car():<8} {car_type:<10} {battery_info:<10}")

    def age_of_car(self):
        current_year = datetime.now().year
        return current_year - self.year

    @classmethod
    def total_cars(cls):
        print(f"\nმანქანების რაოდენობა: {cls.number_of_cars}")

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def car_info(self):
        car_type = "ელექტრო"
        battery_info = f"{self.battery_life} სთ"
        print(f"{self.brand:<15} {self.model:<10} {self.year:<12} {self.age_of_car():<8} {car_type:<13} {battery_info:<10}")

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")