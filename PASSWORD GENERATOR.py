import random
import string

def generate_password(length):
    # define all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # generate the password using random choices from the characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# ask user for password length
length = int(input("Enter the desired password length: "))

# generate and print the password
password = generate_password(length)
print("Your random password is:", password)
