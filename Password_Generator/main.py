import random
from random import randint

print("Password Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


How_many_letters = int(input("How many letters do you like in your password?"))
How_many_Numbers = int(input("How many numbers? "))
How_many_Symbols = int(input("How many symbols"))
password = ""
super_pass = ""

for char in range(1, How_many_letters + 1):
    random_char = random.choice(letters)
    password = password + random_char


for num in range(1, How_many_Numbers + 1):
    random_num = random.choice(numbers)
    password = password + random_num


for sym in range(1, How_many_Symbols + 1):
    random_sym = random.choice(symbols)
    password = password + random_sym


for pas in range(1, len(password) + 1):
    random_pass = random.choice(password)
    super_pass = super_pass + random_pass

print(super_pass)