# Radhe Radhe
import random
from collections import Counter  # To calculate the number of occurrences in the provided sequence for all the elements

words = [
    'apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut',
    'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon'
]

username = input("Enter the player name: ")

word = random.choice(words)
size = len(word)

if __name__ == '__main__':
    print("Start Guessing")
    print("*...Hint...*")
    print(f"It's a fruit with {size} letters")

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letter_guessed = ''
    chances = size + 2
    correct = 0  # Used to tell the number of correctly guessed letters in the selected word.
    flag = 0  # Used to determine whether the word is completely guessed or not.

    try:
        while chances > 0 and flag == 0:
            print()
            print(f"Remaining chances: {chances}")
            guess = input("Enter a letter to guess: ")
            print()
            chances -= 1

            if not guess.isalpha():
                print("Enter only letters!")
                continue

            if len(guess) > 1:
                print("Enter only a single letter!")
                continue

            if guess in letter_guessed:
                print("You have already guessed that letter!")
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letter_guessed += guess

            # Now we will display the progress of our game
            for char in word:
                if char in letter_guessed and Counter(letter_guessed) != Counter(word):
                    print(char, end=' ')
                    correct += 1

                elif Counter(letter_guessed) == Counter(word):
                    print("The word is:", end=' ')
                    print(word)
                    flag = 1
                    print(f"Congratulations {username}!")
                    print("You have guessed the word before your chances ended!")
                    break  # To break out of the for loop

                else:
                    print('_', end=' ')
            print()

        if chances <= 0 and Counter(letter_guessed) != Counter(word):
            print()
            print(f"You lost, {username}")
            print(f"The word was {word}")

    except KeyboardInterrupt:
        print()
        print(f"See you soon, {username}")
        exit()
