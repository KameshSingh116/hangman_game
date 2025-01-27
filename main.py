#Radhe Radhe 
import random
from collections import Counter  #To calculate the number of occurrances in the provided sequence for all the leements

words=['apple', 'banana', 'mango', 'strawberry', 
'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 
'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

username=input("ENter the player name:")

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
    
    try:

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


        if guess in word:
            k=word.count(guess)
            for _ in range(k):
                letter_guessed+=guess

        
        #Now we will be displaying the progresss of our game
        for char in word:
            if char in letter_guessed and Counter(letter_guessed) != Counter(word):
                print(char, end=' ')
                correct +=1
            
            elif (Counter(letter_guessed)==Counter(word)):
                print("The word is:")
                print(word)
                flag=1 
                print(f"Congractulations {username}!") 
                print("You have guessed the word before your chances end!") 

                break #to break out of the for loop
                break #to break out of the while loop
            
            else:
                print('_',end=' ')

     if chances<=0 and Counter(letter_guessed)!=Counter(word):
        print()
        print(f"You lost {username}")
        print(f"The word was {word}")

    except KeyboardInterrupt:
        print()
        print(f"See you soon {username}")
        exit()

            



            



