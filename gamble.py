import random
guess=random.randint(1,3)
print("please enter no. between 1 and 3")
answer=int(input())
if answer == guess:
    print("you win")

else:
    print("you lost")
