from human import Human
from ai import AI
#  TODO: this is similar to how the battlefield was in robots vs dinosaurs


class Game():
    def __init__(self):
        self.user = ""
        #self.opponent = Opponent()
        # super().__init__(User, Opponent, self.player_moves)
        # self.user = User()
        # self.opponent = Opponent()
    
    def game_message(self):
        print('Welcome to rock, paper, scissors, lizard, Spock in a best-of-three format')
        print(' THE RULES:\n  Rock crushes Scissors\n  Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard')

    

game = Game()
message = game.game_message

print(message)