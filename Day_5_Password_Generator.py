import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to the PyPassword Generator!💖")
no_Letters = int(input("How many Letters would you like in your pass?\n"))
no_Numbers = int(input("How many Numbers would you like in your pass?\n"))
no_Symbols = int(input("How many Symbols would you like in your pass?\n"))

password_list = []

for char in range(0 , no_Letters):
    password_list += random.choice(letters)
for char in range(0 , no_Numbers):
    password_list += random.choice(numbers)
for char in range(0 , no_Symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)
final_pass= "".join(password_list)
print(final_pass)