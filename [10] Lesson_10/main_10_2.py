#2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს 
# რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. 
# ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), 
# თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  

# params:[1, 2, 3, 4, 5] 
# output: 120


from functools import reduce

def multiply_list_elements(numbers):
    try:
        return reduce(lambda x, y: x * y, numbers)
    # ვფიქრომ ამ კოდის შემთხვევაში ეგ დაზღვევა ზედმეტია, 
    # თუმცა რახან დავალებაშია მაინც დავწერე. 
    # ... ანუ იმ შემთხვევაში იმუშავებს თუ პარამეტრს გადავცემთ პირდაპირ და შეცდომით.
    except TypeError: 
        return "რაღაც შეცდომა გაიპარა!"

# გავიხსენოთ განვლილი მასალა და მე-7 დავალებისა და ახალი მასალის მიხედვით შემოვიტანოთ შემდეგი:

def get_only_numbers():
    while True:
        try:
            elements = list(map(int, input("\nშეიყვანეთ რიცხვები გამოყოფილი სივრცეებით: ").split()))
            return elements
        except ValueError:
            print("\nუპს, რაღაც ისე არაა! დააკვირდი, ყველა ელემენტი, რიცხვი უნდა იყოს!")


elements = get_only_numbers()

print()
print(elements)
print()
print(multiply_list_elements(elements))
 