import random

def play():
    computer = random.choice(['r', 'p', 's'])
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n") # \n for next line input

    if user == computer:
        return "it's a tie"

    elif is_win(user, computer):
        return "you won!"

    return "you lost!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())