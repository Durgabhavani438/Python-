import random
import string
from words import words

def guess_word(words):
    word=random.choice(words)
    while '-'in word  or ' ' in word:
        word=random.choice(words)
    return word.upper()
def hangman():
    word=guess_word(words)
    print(word)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives=6
    while(len(word_letters)>0 and lives>0):
        print("You have",lives," lives and You have used these letters",' '.join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print("Current word",' '.join(word_list))
        user_input=input("Guess a letter: ").upper()
        if user_input in alphabet-used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives=lives-1
                print("This letter is not in word")

        elif user_input in used_letters:
            print("You have already guessed this number , please try again...")
        else:
            print("invalid character!!")
    if(lives==0):
        print("Sorry!! you dies, the word was: ",word)
    else:
        print("you guessed the word ",word,"!!")
hangman()
    
    
    

