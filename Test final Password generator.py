# if you want to print the output in the same line write end="" in the print statement.
# eg. print(list, end="") and it will print on the same line.


import random

# Lists of letters, numbers, and symbols to use in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print a welcome message for the user
print("Welcome to the PyPassword Generator!")

# Ask the user how many letters, symbols, and numbers they want in their password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create an empty password string to store the characters
password = ""

# Add random letters to the password
for char in range(0, nr_letters):
    random_ch = random.choice(letters)  # Pick a random letter
    password += random_ch  # Add it to the password

# Add random numbers to the password
for numb in range(0, nr_numbers):
    random_nu = random.choice(numbers)  # Pick a random number
    password += random_nu  # Add it to the password

# Add random symbols to the password
for symb in range(0, nr_symbols):
    random_sym = random.choice(symbols)  # Pick a random symbol
    password += random_sym  # Add it to the password

# Print the password before shuffling
print(password)

# Convert the password string to a list of characters so we can shuffle them
pass_list = list(password)

# Shuffle the list to mix up the characters
random.shuffle(pass_list)

# Turn the shuffled list back into a string
password = ''.join(pass_list)

# Print the final, shuffled password
print(password)



#############just for me to keep in mind################
# stars = ""
# for i in range (1,6):
#     star = "*"
#     stars += star
#     print(stars)