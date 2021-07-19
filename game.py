from human import Human
from ai import AI
#  TODO: this is similar to how the battlefield was in robots vs dinosaurs


class Game():
    def __init__(self):
        self.player1 = Human()
        self.plaery2 = AI()
        super().__init__(self)

    
    def game_message(self):
        print('Welcome to rock, paper, scissors, lizard, Spock in a best-of-three format')
        print(' THE RULES:\n Rock crushes Scissors\n Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard')

    # def user_vs_ai(self):




# game = Game()
# message = game.game_message()
