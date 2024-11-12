class Car:
    def __new__(cls):
        # ობიექტის შექმნა __new__ მეთოდით
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        # ინიციალიზაცია: ავტომობილის ბრენდი, მოდელი და წელი
        self._brand = self._get_valid_brand()
        self._model = self._get_valid_model()
        self._year = self._get_valid_year()

    def _get_valid_brand(self):
        while True:
            # ბრენდის შეყვანა და ვალიდაცია
            brand = input("შეიყვანეთ ბრენდი (მხოლოდ ასოები): ")
            if isinstance(brand, str) and brand.isalpha():
                return brand
            else:
                print("ბრენდი უნდა შეიცავდეს მხოლოდ ასოებს.")

    def _get_valid_model(self):
        while True:
            # მოდელის შეყვანა და ვალიდაცია
            model = input("შეიყვანეთ მოდელი: ")
            if isinstance(model, str):
                return model
            else:
                print("მოდელი უნდა იყოს სტრიქონი.")

    def _get_valid_year(self):
        while True:
            # გამოშვების წლის შეყვანა და ვალიდაცია
            try:
                year = int(input("შეიყვანეთ გამოშვების წელი (1886 - 2024): "))
                if 1886 <= year <= 2024:
                    return year
                else:
                    print("წელი უნდა იყოს 1886 - 2024 დიაპაზონში.")
            except ValueError:
                print("წელი უნდა იყოს მთელი რიცხვი.")

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

# გამოყენება
car = Car()
print(f"\nავტომობილი: {car.brand} {car.model} {car.year}")
