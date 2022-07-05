import random

def Guessnoforcomp(x):
    low=1
    high=x
    feedback=""
    while(feedback!="c"):
        if(low!=high):
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too low(L) or too high(H) or correct(C)??: ".lower())
        if(feedback=="h"):
            high=guess-1
        elif(feedback=="l"):
            low=guess+1
        
    print(f"Yayyy, congrats you guessed {guess} correctly...")
n=int(input("Enter number for range: "))
Guessnoforcomp(n)
        

