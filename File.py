import random 
import time
def randomm():
    while True:
        user = input("rock , paper , scissor or q to end the game : ")
        if user == "q":
            break
        computer = random.choice(["rock","paper","scissor"])
        print(f"Computer Choice : {computer}")
        time.sleep(2)
        if user == computer:
            print("It is a tie")
        elif(user == "rock" and computer == "scissor") or (user == "paper" and computer == "rock") or (user == "scissor" and computer == "paper"):
            print("You Win")
        else :
            print("Computer Wins")

def guessing():
    while True:
        print("It is a Random Guessing Game ")
        print("Curious about it Right !!!!")
        time.sleep(5)
        b = random.randint(1,10)
        print("Guess the Secret number between 1 & 10")
        time.sleep(2)
        guess = int(input("Enter the Guess Number"))
        if guess == b:
            print("Congratulations you have choosen the Correct Numebr")
        else:
            print("Sorry you have choosen the wrong number")
            time.sleep(3)
            print("The Number is :",b)

def choice():
    print("Welcome the world of Games".center(150))
    print("Tell Us What Game you Want to Play")
    time.sleep(3)
    print("RandomNumber Guessing Game  :  Enter [ 1 ]")
    print("Rock Paper Scissior : Enter [ 2 ]")
    n = int(input("Enter the Choice of Your Game"))
    if n == 1:
        randomm()
    elif n ==2:
        guessing()
choice()
