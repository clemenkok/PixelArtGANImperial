import random
import string


password_number = int(input("How many passwords do you want?"))


def GENERATOR():
    password_length = 8
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    for x in range(password_length):
        password.append(random.choice(password_characters))
    print(''.join(password))


for y in range(password_number):
        GENERATOR()
