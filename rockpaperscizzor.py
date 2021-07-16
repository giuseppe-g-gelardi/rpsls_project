# using this for logic flow on how to create more advanced game
#simpel rock paper scissors

import random

def play():
    user = input('r, s, p')
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'Tie Game!'

    if win_lose(user, computer):
        return 'user won!'
    return 'you lost!!!!!!!!!!!!!'

def win_lose(player, ai):
    if (player == 'r' and ai == 's') or (player == 's' and ai == 'p') or (player == 'p' and ai == 'r'):
        return True


print(play())


