from players import Players
from human import Human
from ai import AI



class Game:
    def __init__(self):
        self.player1 = Human(input('hello player1, what is your name?  '))
        self.player2 = AI("opponent")

    def run_game(self):
        self.game_message()
        self.multiplayer()
        self.outcome()
        self.restart()

    def game_message(self):
        print('Welcome to rock, paper, scissors, lizard, Spock in a best-of-three format')
        print(' THE RULES:\n Rock crushes Scissors'
              '\n Scissors cuts Paper'
              '\n Paper covers Rock'
              '\n Rock crushes Lizard'
              '\n Lizard poisons Spock'
              '\n Spock smashes Scissors'
              '\n Scissors decapitates Lizard')


    def gesture_compare_singleplayer(self):
        while (self.player1.score < 3 and self.player2.score < 3):
            self.player1.gestures()
            self.player2.computer_choice()
            
            if self.player1.choice == self.player2.opponent_random_move:
                    print("tie!, go again!")
       
            elif (self.player1.choice == 'rock' and self.player2.opponent_random_move == 'scissors') or \
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
                    print(f'{self.player1.choice} beats! {self.player2.opponent_random_move} player 1 won that round!!')
                    print(f'score is Player 1: {self.player1.score} Player 2: {self.player2.score}')
                    return self.gesture_compare_singleplayer()
            else:
                    self.player2.score += 1
                    print(f'{self.player2.opponent_random_move} beats! {self.player1.choice} player 2 won that round!!')
                    print(f'score is Player 1: {self.player1.score} Player 2: {self.player2.score}')


    def outcome(self):
        if self.player1.score == 3 or self.player2.score == 3:
            if self.player1.score > self.player2.score:
                print("Player1 has won the game")
                
            else:
                print("Player2 has won the game")
                


    def multiplayer(self):
        userInput = input("would you like to play multiplayer? yes or no: ").lower()
        if userInput == "yes":
            self.player2 = Human(input('hello player2, what is your name?'))
            self.gesture_compare_multiplayer()
        elif userInput == 'no':
            self.gesture_compare_singleplayer()
        else:
            print('invalid input, please type yes or no')
            self.multiplayer()          


    def gesture_compare_multiplayer(self):
        while (self.player1.score < 3 and self.player2.score < 3):
            self.player1.gestures()
            self.player2.gestures()
            if self.player1.choice == self.player2.choice:
                print("tie!, go again!")
                
            elif (self.player1.choice == 'rock' and self.player2.choice == 'scissors') or \
                    (self.player1.choice == 'scissors' and self.player2.choice == 'paper') or \
                    (self.player1.choice == 'paper' and self.player2.choice == 'rock') or \
                    (self.player1.choice == 'rock' and self.player2.choice == 'lizard') or \
                    (self.player1.choice == 'lizard' and self.player2.choice == 'spock') or \
                    (self.player1.choice == 'spock' and self.player2.choice == 'scissors') or \
                    (self.player1.choice == 'lizard' and self.player2.choice == 'paper') or \
                    (self.player1.choice == 'paper' and self.player2.choice == 'spock') or \
                    (self.player1.choice == 'spock' and self.player2.choice == 'rock') or \
                    (self.player1.choice == 'scissors' and self.player2.choice == 'lizard'):
                self.player1.score += 1
                print(f'{self.player1.choice} beats! {self.player2.choice} player 1 won that round!!')
                print(f'score is Player 1: {self.player1.score} Player 2: {self.player2.score}')
            else:
                self.player2.score += 1
                print(f'{self.player2.choice} beats! {self.player1.choice} player 2 won that round!!')
                print(f'score is Player 1: {self.player1.score} Player 2: {self.player2.score}')
            

    def restart(self):
        self.play_again = input('would you like to play agian? yes or no: ').lower()
        if self.play_again == 'yes':
            self.player1.score = 0
            self.player2.score = 0
            self.run_game()
        elif self.play_again == 'no':
            print('thanks for playing!')
        else:
            print('invalid input please, choose yes or no!')
            self.restart()