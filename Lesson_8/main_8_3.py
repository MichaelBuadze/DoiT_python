# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.

n = int(input("\n შეიყვანეთ სასურველი რიცხვი: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0 :
        return " თქვენ შეიყვანეთ უარყოფითი რიცხვი"
    else:
        return n * factorial(n - 1)

print(factorial(n))
