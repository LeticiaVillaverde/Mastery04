print ("I have a number between 1 and 100")
import random
cpu= random.choice(range(1,100))
num=int (input("Please guess a number between 1 and 100: "))
cont = 1
while num != cpu:
    cont = cont + 1
    if num>cpu:
        print("I'm sorry but",num,"is too high")
    else:
        print("I'm sorry but",num,"is too low")
    num = int(input("try again: "))

print ("You got it!, The right answer is indeed",num)
print ("You made ",cont," guesses to get the right number")
