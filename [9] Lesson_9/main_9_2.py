#2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და 
# აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს 
# შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

# მეთოდი 1
def sum_list(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result = sum_list(numbers)
print(result)

# თავისფალი სივცე
print()

# მეთოდი 2 

def sum_of_list(numbers):
    return sum(numbers)

numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print(sum_of_list(numbers))

# თავისფალი სივცე
print()

# მეთოდი 3

def sum_list(args):
  total = 0
  for num in numbers:
    total += num
  return total

numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result = sum_list(numbers)
print(result)

# თავისფალი სივცე
print()

# მეთოდი 3.1

def sum_list(*args):
  total = 0
  for num in numbers:
    total += num
  return total

numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result = sum_list(*numbers)
print(result)