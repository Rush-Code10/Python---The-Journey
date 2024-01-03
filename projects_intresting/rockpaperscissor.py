import random
rounds = int(input("Enter no. of rounds you want to play: "))
pts_computer = 0
pts_player = 0
n = 1
while True:
    print("---------------------------------------------")
    print(n)
    n = n+1
    player_choice = input("Enter (rock,paper,scissor) :")
    choices = ["rock","paper","scissor"]
    computer_choice = random.choice(choices)
    print("Computer Choice : " ,computer_choice)
    if (player_choice == "rock" and computer_choice == "paper") or (player_choice == "scissor" and computer_choice == "rock") or (player_choice == "paper" and computer_choice == "scissor") :
        pts_computer = pts_computer+1
    if (player_choice == "rock" and computer_choice == "scissor") or (player_choice == "scissor" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock") :
        pts_player = pts_player+1

    print("---------------------------------------------")
    print("Score")
    print("Player - ",pts_player)
    print("Computer - ",pts_computer)

    if pts_player == rounds or pts_computer == rounds:
        print(">>>>>>>>>><<<<<<<<<<")
        print("Player Points : ", pts_player)
        print("Computer Points : ", pts_computer)
        if pts_player > pts_computer:
            print("# PLAYER WON")
        else:
            print("# COMPUTER WON")
        print(">>>>>>>>>><<<<<<<<<<")
        break
