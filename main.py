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
