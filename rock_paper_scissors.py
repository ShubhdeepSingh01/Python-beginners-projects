import random
'''
rock = 1
paper = -1
scissors = 0

'''
computer = random.choice([1,-1,0])

yourchoice = input("Enter your choice: ")
yourDict = {"s":0,"p":-1,"r":1,"S":0,"P":-1,"R":1}
reverseDict = {0:"scissors",1:"rock",-1:"paper"}

You = yourDict.get(yourchoice)

print(f"Computer choose {reverseDict[computer]}\nYou choose {reverseDict[You]}")

if (computer == You):
    print("Its a draw")

else:

    if(computer == 1 and You == -1):
        print("You win!")

    elif(computer == 1 and You == 0):
        print("You loose")

    elif(computer == 0 and You == 1):
        print("You win!")

    elif(computer == 0 and You == -1):
        print("You loose")

    elif(computer == -1 and You == 1):
        print("You loose")

    elif(computer == -1 and You == 0):
        print("You win!")

    else:
        print("Something went wrong")




