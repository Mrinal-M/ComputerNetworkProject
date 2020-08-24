# ComputerNetworkProject
This is a computer network based simulation of a  quiz game, where the participants are the clients and the host is the server.
The game is played by 3 players. Whenever a player gets 5 points the game ends.
Initially the host will display a question. The player who responds "bz" fastest can answer the question. If the answer is correct then the point of the player is incremented by one, otherwise the host goes to the next question.
This process is repeated till one of the player wins.

This game contains two programs- server.py and client.py
server.py handles the host side of the game. It takes care of all the things that needs to be done during the game.
client.py handles the participant side of the game. It takes care of pressing buzzer and replying.
