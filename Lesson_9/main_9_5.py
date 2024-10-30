# 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, 
# რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს 
# მის შებრუნებულ (revers) სტრიქონს (მაგალითად  input: Hello   Output: olleH)

s = input("შეიყვანე სასურველი სიტყვა: ")

def reverse_str(s):
    if not s:
        return s
    else:
        return reverse_str(s[1:]) + s[0]
reversed_str = reverse_str(s)
print(reversed_str)

