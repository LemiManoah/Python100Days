import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '?', '~', '`', '\\', '|']


print("welcome to our password generator")
password_length = int(input("Enter the desired length of the password: "))
nr_letters = int(input("how many letters would you like in your password"))
nr_numbers = int(input("how many numbers would you like in your password"))
nr_symbols = int(input("how many symbols would you like in your password"))


#easy level(the password is in order of random letters first, the random numbers, then random symbols)
#initialize password to an empty string
password = ""
#select a random number of selected letters from the letters list
for char in range(1, nr_letters + 1):
    password = password + random.choice(letters)
    
for char in range(1, nr_numbers + 1):
    password = password + random.choice(numbers)
    
for char in range(1, nr_symbols + 1):
    password = password + random.choice(symbols)
print(password)


#hard level (random numbers, numbers and symbols all mixed up)
#we shall initialize a list instead of a password variable
password_list = []
#select a random number of selected letters from the letters list
for char in range(1, nr_letters + 1):
    password_list = password + random.choice(letters)
    
for char in range(1, nr_numbers + 1):
    password_list = password + random.choice(letters)
    
for char in range(1, nr_symbols + 1):
    password_list = password + random.choice(symbols)
    
random.shuffle(password_list)

password = ""
for char in password_list:
    password = password + char
    
print(f"Your password is: {password}")
    


