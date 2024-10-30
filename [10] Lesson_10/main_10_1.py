#1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) 
# და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

def zip_lists(list1, list2):
    return [str(item) for item in zip(list1, list2)]

# გამოყენება

print(zip_lists([1, 2, 3], ['a', 'b', 'c']))


