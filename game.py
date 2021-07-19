from user import User
from opponent import Opponent
#  TODO: this is similar to how the battlefield was in robots vs dinosaurs


class Game(User, Opponent):
    def __init__(self):
        super().__init__(User, Opponent)

    @staticmethod  # ! method is static for testing only
    def game_message():
        print("method inside the game class")


Game.game_message()
# TODO add run_game() method

