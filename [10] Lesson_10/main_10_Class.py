# sumOfNumbers = lambda x, y, z: x + y + z
# print(sumOfNumbers(1, 4, 6))

# some = input("enter some word in lowercase: ")
# testfunc = lambda some: some.capitalize() + "!"

# print(testfunc(some))


# # მონაცემების შეყვანა კონსოლიდან
# data_tuple = tuple(map(int, input("\nშეიყვანეთ რიცხვები გამოყოფილი სივრცეებით: ").split()))
# print()

# # სიის შექმნა უნიკალური ელემენტებით
# que_list = list(set(data_tuple))
# print(que_list)
# print()

# #3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# # params: [1, 2, 3, 4, 5, 6, 7]
# # outputs: [1, 3, 5, 7]

# odd_numbers = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))

# # გამოყენება
# print(odd_numbers(que_list))

from functools import reduce

def multiply_list_elements(numbers):
    try:
        return reduce(lambda x, y: x * y, numbers)
    except TypeError as e:
        if "unsupported operand type(s) for *: 'int' and 'str'" in str(e):
            # მოძებნა ელემენტის, რომელიც არ არის რიცხვი
            for i, num in enumerate(numbers):
                if not isinstance(num, (int, float)):
                    return f"შეცდომა: ელემენტი '{num}' არ არის რიცხვი (ინდექსი: {i}). ყველა ელემენტი რიცხვი უნდა იყოს!"
        else:
            return f"უცნობი შეცდომა: {e}"
    return "უპს, რაღაც ისე არაა! დააკვირდი, ყველა ელემენტი, რიცხვი უნდა იყოს!"

# გამოყენება
elements = list(map(int, input("\nშეიყვანეთ რიცხვები გამოყოფილი სივრცეებით: ").split()))
print()
print(elements)
print()
print(multiply_list_elements(elements))