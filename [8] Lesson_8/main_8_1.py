#1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, 
# და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

n = int (input("შეიყვანეთ სასურველი რიცხვი: "))

def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:n]  # ამოჭრის, თუ n არის ნაკლები ან ტოლი 2-ის

print(fibonacci_sequence(n))