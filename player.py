class Player:
    def __init__(self, player, name):
        self.player = player
        self.name = name
   
    def choice(self, gestures):   
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        print(gestures[0])
        print(gestures[1])
        print(gestures[2])
        print(gestures[3])
        print(gestures[4])
