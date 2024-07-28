import random

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangman_count = 0

word_bank = ["hangman", "elephant", "gorilla", "man", "replacement", "Nataly",
             "maximo", "pizza", "strange", "zebra", "tiger", "specific"]


# Selects a secret word from the word_bank for the player to guess.
secret_word = random.choice(word_bank)

# Obfuscates secret word
hidden_word = []
for letter in range(0, len(secret_word)):
    hidden_word.append("-")

user_guesses = []

while hangman_count < len(hangman_pics):
    print(hangman_pics[hangman_count])

    # Prints a list of the users guesses.
    print("You're guesses: ")
    print(sorted(user_guesses))

    # Prints the hidden word.
    print("Secret Word:", "".join(hidden_word))

    # Takes in user guess and records it in a list
    user_guess = input("Enter a letter: ").lower()

    # Checks if the player already guessed the same letter.
    # The loop breaks if the users current guess is not in the list.
    while True:
        if user_guess in user_guesses:
            print("You're guesses: ")
            print(user_guesses)
            print("You already used this letter. Pick another one.")
            print("Secret Word:", "".join(hidden_word))
            user_guess = input("Enter a letter: ").lower()
        elif user_guess not in user_guesses:
            break

    print(sorted(user_guesses))
    user_guesses.append(user_guess)
    good_guess = False

    # Cycles through each letter in the secret_word list
    for letter in range(0, len(secret_word)):

        # Checks to see if the man has been hung.
        if hangman_count == 6:
            print("You Lost!")
            break

        # Checks if the user guessed a letter correctly.
        elif user_guess == secret_word[letter]:
            hidden_word[letter] = user_guess
            good_guess = True

        # If the user did not guess a single letter correctly. Results in the man getting hung.
        elif good_guess == False and letter == len(secret_word) - 1:
            hangman_count += 1
            break

