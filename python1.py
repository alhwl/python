import random

x = input("pick a number between 1 and 100: ")
y = random.randint(1,100)

print("you picked " + x + " and the number " + str(y) + " was genorated")
print(f"You picked {x} and the number genorated was {y}".format(x,y))

if int(x) < y:
    print("Too Low!")
if int(x) > y:
    prin("Too high")
if int(x) == y:
    print("correct!")