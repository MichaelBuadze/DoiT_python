# მოცემულია სია. 
# კონსოლიდან შევიტანოთ რიცხვი და ტექსტი. თუ შეტანილი 
# რიცხვი სიაშია წავშალოთ. ასევე წავშალოთ შეტანილი ტექსტი, თუ იგი 
# მთავარი სიის ქვესიაშია.


my_list = [14, 'text', 41, 3.67, 'Boolean type', [16, 54, 'city']]

# მომხმარებლისგან მონაცემების მიღება
number = eval(input("Enter a number: "))
text = input("Enter a text: ")

# რიცხვის წაშლა მთავარი სიიდან
if number in my_list:
    my_list.remove(number)

# გადავხედოთ სიის ყველა ელემენტს
for item in my_list:
    if type(item) == list:
        # თუ ტექსტი ამ სიაშია, წავშალოთ
        if text in item:
            item.remove(text)


# შედეგის დაბეჭდვა
print("Modified list:", my_list)

