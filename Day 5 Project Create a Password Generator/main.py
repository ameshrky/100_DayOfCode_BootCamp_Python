import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for letter in range(nr_letters):
    password += random.choice(letters)
for symbol in range(nr_symbols):
    password += random.choice(symbols)
for number in range(nr_numbers):
    password += random.choice(numbers)
print(f"Your 'Easy Version' password is: {password}")

password_char = list(password)
random.shuffle(password_char)
password_hard_version = ''.join(password_char)

print(f"Your 'Hard Version' password is - V1: {password_hard_version}")

password_hard_version = ""
for _ in range(len(password)):
    idx = random.randrange(len(password_char))
    password_hard_version += password_char.pop(idx)
print(f"Your 'Hard Version' password is - V2: {password_hard_version}")
