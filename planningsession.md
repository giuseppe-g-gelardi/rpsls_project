OBJECTIVE:

1. develop an algorith for the entire game
2. come up with the classes needed for the project (with an idea of where inheritance will be used)

ALGORITHM:

1. display a welcome and rules of the game
2. select a single player (human vs AI) OR multiplayer (human vs human)
3. display a list of gesture options
4. players select their gestures
5. compare the gestures and see which one wins 6. show the winner! (also check for ties)
6. show the winner of the round and track the score of the winner
7. see if anyone hs won the entire game
8. if not, play another round
9. when someone has won best of three
10. display the winner
11.

CLASSES:

1. game (like the battle field, ocrhestrates the flow of the game)
2. player (parent)
3. AI (child of player)
4. human (child of player)
5. main.py (will always be the entrypoint into the application and creates instances of our classes)
