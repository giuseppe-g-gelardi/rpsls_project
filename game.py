from players import Players
from human import Human
from ai import AI


#  TODO: this is similar to how the battlefield was in robots vs dinosaurs


class Game:
    def __init__(self):
        self.player1 = Human("bob")
        self.player2 = AI("goblin")
        # super().__init__(self)

    def run_game(self):
        self.game_message()
        self.gesture_compare()
        self.outcome()

    def game_message(self):
        print('Welcome to rock, paper, scissors, lizard, Spock in a best-of-three format')
        print(' THE RULES:\n Rock crushes Scissors'
              '\n Scissors cuts Paper'
              '\n Paper covers Rock'
              '\n Rock crushes Lizard'
              '\n Lizard poisons Spock'
              '\n Spock smashes Scissors'
              '\n Scissors decapitates Lizard')

    # method to compare the gestures
    def gesture_compare(self):
        self.player1.gestures()
        self.player2.choice()
        while (self.player1.score or self.player2.score) < 3:
            
            if self.player1.choice == self.player2.opponent_random_move:
                print("tie!, go again!")
                return False
            if (self.player1.choice == 'rock' and self.player2.opponent_random_move == 'scissors') or \
                    (self.player1.choice == 'scissors' and self.player2.opponent_random_move == 'paper') or \
                    (self.player1.choice == 'paper' and self.player2.opponent_random_move == 'rock') or \
                    (self.player1.choice == 'rock' and self.player2.opponent_random_move == 'lizard') or \
                    (self.player1.choice == 'lizard' and self.player2.opponent_random_move == 'spock') or \
                    (self.player1.choice == 'spock' and self.player2.opponent_random_move == 'scissors') or \
                    (self.player1.choice == 'lizard' and self.player2.opponent_random_move == 'paper') or \
                    (self.player1.choice == 'paper' and self.player2.opponent_random_move == 'spock') or \
                    (self.player1.choice == 'spock' and self.player2.opponent_random_move == 'rock') or \
                    (self.player1.choice == 'scissors' and self.player2.opponent_random_move == 'lizard'):
                self.player1.score += 1
            else:
                self.player2.score += 1
            
            return self.gesture_compare()



    def outcome(self):
        if self.player1.score or self.player2.score == 3:
            if self.player1.score > self.player2.score:
                print("Player1 has won the game")
                play_again = input("yes or no: ")
                if play_again == "yes":
                    return self.run_game()
            else:
                print("Player2 has won the game")
                play_again = input("Would you like to play again? yes or no: ")
                if play_again == "yes":
                    return self.run_game()
