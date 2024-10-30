#3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# მაგ.:
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

# მონაცემების შეყვანა კონსოლიდან
def get_numbers():
    while True:
        try:
            data_by_you = list(map(int, input("\nშეიყვანეთ რიცხვები გამოყოფილი სივრცეებით: ").split()))
            print()
            return data_by_you
        except ValueError:
            print("\nშეყვანილი ელემენტი, მხოლოდ რიცხვი უნდა იყოს!")

data_by_you = get_numbers()

# უნიკალური list 
uni_list = list(set(data_by_you))
print(uni_list)
print()

# კენტი რიცხვების lambda ფუნქციის გამოყენებით გაფილტრვა
odd_numbers = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers)) 

# გამოყენება
# შესაძლებელია პირდაპირ სიის გადაცემა
# print(odd_numbers([1, 2, 3, 4, 5, 6, 7]))

print(odd_numbers(uni_list))