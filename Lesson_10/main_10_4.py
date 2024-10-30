#4. დაწერეთ პითონის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). 
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. 
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']


def filter_by_ending(strings, ending):

  # აბრუნებს სიის ელემენტებს, რომლებიც მთავრდება მითითებული სტრიქონით.

  # Args:
  #   strings: სტრიქონების სია.
  #   ending: სასურველი საფილტრი დაბოლოება.

  # Returns:
  #   დაბოლოებით დაფილტრული სტრიქონების სია.


  try:
    return list(filter(lambda x: x.endswith(ending), strings))
  except AttributeError:
    print("სია მხოლოდ სტრიქონებს უნდა შეიცავდეს")
    return None

# მაგალითი:
result = filter_by_ending(['hello', 'world', 'coding', 'nod'], 'ing') 
# შესაძლებელია აქაც კონსოლიდან შევიყვანოთ სიტყვები თუმცა ახლა 03:22 საათია, თან პარასკევი, შაბათ-კვირას ვერ ვიცლი და იყოს ასე :) 
print(result)  # გამოიტანს: ['coding']