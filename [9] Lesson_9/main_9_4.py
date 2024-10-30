# 4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, 
# რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს  
# ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, 
# უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).

# რეკურსიული ფუნქციის პირველი მეთოდი:

def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits(number // 10)

print(sum_of_digits(12345))  # შედეგი: 15

# რეკურსიული ფუნქციის მეორე მეთოდი:

def sum_digits(number):
    sum_num = 0
    for digit in str(number):
        sum_num += int(digit)
    return sum_num

print(sum_digits(12345))  # შედეგი: 15

