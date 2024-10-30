# 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list_1 = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს შემდეგ ნაბიჯებს:

# a. დაბეჭდავს 210-ის ინდექსს;
 
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;

# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist_1-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

# მინიშნება: სიის გასუფთავება – arr.clear()

# Python program to perform the given tasks

# Initialize the list
my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# a. Print the index of 210
index_of_210 = my_list_1.index(210)

# b. Add "hello" to the last element (which is a list inside the main list)
my_list_1[-1].append("hello")

# c. Remove the element at index 2 and print the list
my_list_1.pop(2)

# d. Create a new list my_list_2 with the values of my_list_1, clear my_list_2, and print both lists
my_list_2 = my_list_1.copy()
my_list_2.clear()

(my_list_1, my_list_2, index_of_210)
