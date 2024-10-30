#1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის 
# UTF-8 დაშიფრულ ვერსიას.

txt = "გამარჯობა, მსოფლიო!"
encoded_txt = txt.encode('utf-8')
print(encoded_txt)

decoded_txt = encoded_txt.decode('utf-8')
print(decoded_txt)