import random

replay = "Yes"

while True:

    if replay == "No":
        break

    print("WELCOME TO ROCK, PAPER SCISSORS! \n")
    playerHand = input("Choose Your Hand: Rock, Paper, Scissors?!")

    hands = ["Rock", "Paper", "Scissors"]
    computerHand = random.choice(hands)

    print("\n OKAY! Since You opted for {playerHand} & the Computer opted for {computerHand}: \n")
    print("\n THE WINNER")

    if playerHand == computerHand:
        print("S ARE: You & the Computer!")

    elif playerHand == "Rock":
        if computerHand == "Scissors":
            print("IS: You!")
        else:
            print("IS: the Computer")

    elif playerHand == "Paper":
        if computerHand == "Rock":
            print("IS: You!")
        else:
            print("IS: the Computer")

    elif playerHand == "Scissors":
        if computerHand == "Paper":
            print("IS: You!")
        else:
            print("IS: the Computer")

replay = input("\n Would like to play another round? Enter Yes or No")

