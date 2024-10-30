# მოცემულია სია. 
# კონსოლიდან შევიტანოთ რიცხვი და ტექსტი. თუ შეტანილი 
# რიცხვი სიაშია წავშალოთ. ასევე წავშალოთ შეტანილი ტექსტი, თუ იგი 
# მთავარი სიის ქვესიაშია.


my_list = [14, 'text', 41, 3.67, 'Boolean type', [16, 54, 'city']]

# მომხმარებლისგან რიცხვის მიღება
number = input("Enter a number: ")

# რიცხვის კონვერტაცია (თუ შესაძლებელია)
if number.isdigit():
    number = int(number)
else:
    print("Invalid number entered.")
    number = None

# მომხმარებლისგან ტექსტის მიღება
text = input("Enter a text: ")

# თუ რიცხვი სიაშია, წავშალოთ
if number is not None and number in my_list:
    my_list.remove(number)

# გადავხედოთ სიის ყველა ელემენტს
for item in my_list:
    if type(item) == list:
        # თუ ტექსტი ამ სიაშია, წავშალოთ
        if text in item:
            item.remove(text)

# შედეგის დაბეჭდვა
print("Modified list:", my_list)


