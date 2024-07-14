import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "#", "%", "^", "&", "*"]

character_choice = ["alphabet", "symbols", "numbers"]
password = ""

password_length = int(input("Length of Password: "))


while len(password) < password_length:
    random.choice(character_choice)
    if random.choice(character_choice) == "alphabet":
        password = password + random.choice(alphabet)
    elif random.choice(character_choice) == "symbols":
        password = password + random.choice(symbols)
    elif random.choice(character_choice) == "numbers":
        password = password + random.choice(numbers)

print(password)


