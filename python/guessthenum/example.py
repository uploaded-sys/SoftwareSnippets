import random
print("1 to 100 numbergusser game")
randomnum = random.randint(1,100)
print(randomnum)
while True:
    ans = int(input("Guess the number between 1 and 100:"))
    if ans == randomnum:
        print("you won the game the answer was" ,randomnum)
        break
    elif ans < randomnum:
        print("you have no high dreams i guess ")
    elif ans > randomnum:
        print("you you think too high")