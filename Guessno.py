import random
def guessno(x):
    Random_num=random.randint(1,x)
    guess=0
    while(guess!=Random_num):
        guess=int(input(f"guess a number between 1 and {x}: "))
        if(guess<Random_num):
            print("Sorry ,Guess again, Number is too low.")
        elif(guess>Random_num):
            print("Sorry, Guess again, Number is too high")
    print(f"Yayy Congratulations.. You guesses the number {Random_num} correctly")
n=int(input("Enter number for range: "))
guessno(n)