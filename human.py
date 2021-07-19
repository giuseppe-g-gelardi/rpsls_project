from player import Player

class Human(Player):
    def __init__(self, player1):
        self.player1 = ''
        print('this works')

    def player_choice(self):
        self.choice = input('Please choose: R for rock, P for paper, S for scissors, L for lizzard, and SP for Spock ').toLowerCase()
        while self.choice is not ['r', 's', 'p', 'l', 'sp']:
            print('sorry invalid choice! Please select r, s, p, l, or sp!')
            self.choice = input('Please choose: R for rock, P for paper, S for scissors, L for lizzard, and SP for Spock ').toLowerCase()
            
            return self.choice
        
        print(self.choice)
        return self.choice

test = player_choice()

print(test)