#!/usr/bin/python3
import random
move_list = []
possible_data = ["rock","paper","scissors"]
def win(p1_choice,p2_choice):
    if p1_choice == "rock" and p2_choice == "rock":
        return "DRAW"
    elif p1_choice == "rock" and p2_choice == "paper":
        return "PC"
    elif p1_choice == "rock" and p2_choice == "scissors":
        return "HUMAN"
    elif p1_choice == "paper" and p2_choice == "paper":
        return "DRAW"
    elif p1_choice == "paper" and p2_choice == "rock":
        return "HUMAN"
    elif p1_choice == "paper" and p2_choice == "scissors":
        return "PC"
    elif p1_choice == "scissors" and p2_choice == "scissors":
        return "DRAW"
    elif p1_choice == "scissors" and p2_choice == "rock":
        return "PC"
    elif p1_choice == "scissors" and p2_choice == "paper":
        return "HUMAN"
choice = input("rock?paper?scissors\n>")
move_list.append(choice)
# pc_choice = "paper"
pc_choice = possible_data[random.randint(0,2)]
move_list.append(pc_choice)
notwins = []
with open("notwin.txt" , "r") as f:
    for i in f.read().splitlines():
        notwins.append(i.split(','))
# print(notwins)
# print(move_list)
while move_list in notwins:
    # print(move_list)
    # print(notwins)
    pc_choice = possible_data[random.randint(0,2)] 
    move_list.pop()
    move_list.append(pc_choice)
else:
    print(f"i choose {pc_choice}")
result =  win(choice,pc_choice)
# print(result)
if result == "DRAW":
    print("its a draw")
    with open("notwin.txt" , "a") as f:
        f.write(",".join(move_list)+"\n")
elif result == "HUMAN":
    print("you won")
    with open("notwin.txt" , "a") as f:
        f.write(",".join(move_list)+"\n")
elif result == "PC":
    print("I won")