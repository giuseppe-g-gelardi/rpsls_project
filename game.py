from user import User
from opponent import Opponent


class Game(User, Opponent):
    def __init__(self):
        super().__init__(User, Opponent)
        

# TODO add run_game() method
    def game(self, user, opponenet):
        
