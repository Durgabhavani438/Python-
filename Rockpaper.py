import random
def play():
    user=input("'r' For rock ,'s' for scissors ,'p' for paper ...\Enter you'r choice: ")
    computer=random.choice(['r','p','s'])
    if(user==computer):
        return "It's a die"
    if(iswon(user,computer)):
        return "You won!!"
    return "You lost!!"
def iswon(user,computer):
    if(user=='r' and computer=='s')or (user=='p' and computer=='r') or (user=='s' and computer=='p'):
        return True
print(play())
