#Radhe Radhe 
import random
from collections import Counter  #To calculate the number of occurrances in the provided sequence for all the leements

words=['apple', 'banana', 'mango', 'strawberry', 
'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 
'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

word=random.choice(words)
size=len(word)

if __name__=='__main__':
    print("Start Guessing")
    print("*...Hint...*")
    print(f"Its a fruit with {size} letters")

    for i in word:
        print('_', end=' ')
    print()

    playing=True
    letter_guessed=''
    chances=size+2
    correct=0  #used to tell the number of correctly guessed letters in the selected word.
    flag=0     #used to determine whether the word is complete;ly guessed or not.
    

    while(chances>0) and flag==0:

        try:
            guess=str(input("Enter the letter to guess:"))

        except:
            print("Enter only letters!")
            continue

        if not guess.isalpha():
            print("Enter only letters!")

        elif len(guess)>1:
            print("Enter only single letter!")
            continue

        elif guess in letter_guessed:
            print("You have already guessed the letter!")
            continue

        

        

