class Player:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.opponent = player2
        self.choice(self) # ? would choices be gestures?

        
    def choice(self, gestures):   
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        print(choice[0])
        print(choice[1])
        print(choice[2])
        print(choice[3])
        print(choice[4])
