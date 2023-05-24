#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_list = []
letters_list = []
numbers_list = []
symbols_list = []
for i in range(len(letters)):
  while len(letters_list) < nr_letters:
    letters_list.append(random.choice(letters))

for i in range(len(numbers)):
  while len(numbers_list) < nr_numbers:
    numbers_list.append(random.choice(numbers))

for i in range(len(symbols)):
  while len(symbols_list) < nr_symbols:
    symbols_list.append(random.choice(symbols))

easy_list = letters_list + symbols_list + numbers_list
print(easy_list)

#using join to convert list to string

easy_password = ''.join(easy_list)
print(easy_password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_list = easy_list
random.shuffle(hard_list)
print(hard_list)
hard_password = ''.join(hard_list)
print(hard_password)