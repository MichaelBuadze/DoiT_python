class Car:
    def __new__(cls, brand, model, year):
        # ობიექტის შექმნა `__new__` მეთოდით
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        # ინიციალიზაცია: ავტომობილის ბრენდი, მოდელი და გამოშვების წელი
        self._brand = None
        self._model = None
        self._year = None
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        # ბრენდის მიღება
        return self._brand

    @brand.setter
    def brand(self, value):
        # ბრენდის ვალიდაცია: მხოლოდ სტრიქონი და ასოები
        if isinstance(value, str) and value.isalpha():
            self._brand = value
        else:
            raise ValueError("Brand უნდა იყოს ასოებისგან შემდგარი სტრიქონი")

    @property
    def model(self):
        # მოდელის მიღება
        return self._model

    @model.setter
    def model(self, value):
        # მოდელის ვალიდაცია: მხოლოდ სტრიქონი
        if isinstance(value, str):
            self._model = value
        else:
            raise ValueError("Model უნდა წარმოადგენდეს სტრიქონს")

    @property
    def year(self):
        # გამოშვების წლის მიღება
        return self._year

    @year.setter
    def year(self, value):
        # წლის ვალიდაცია: მთელი რიცხვი და გარკვეული წლების დიაპაზონი
        if isinstance(value, int) and 1886 <= value <= 2024:
            self._year = value
        else:
            raise ValueError("Year უნდა იყოს მთელი რიცხვი, 1886-სა და მიმდინარე წელიწადს შორის.")

# გამოყენება
car = Car("Toyota", "Corolla", 2020)
print(car.brand, car.model, car.year)  # Output: Toyota Corolla 2020
