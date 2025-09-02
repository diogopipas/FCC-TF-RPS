# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import RPS_game

def player(prev_play, opponent_history=[]):
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    choice = ["R", "P", "S"]
    guess = choice[len(opponent_history) % 2]
    #quincy
    if opponent_history[:5] == ["", "R", "P", "P", "S"]:
        guess = counter[RPS_game.quincy(prev_play)]
        return guess
    #mrugesh
    elif opponent_history[:2] == ["", "P", "P", "P"]:
        guess = counter[RPS_game.mrugesh(prev_play)]
        return guess
    #kris
    elif opponent_history[:5] == ["", "P", "S", "R", "P", "S"]:
        guess = counter[RPS_game.kris(prev_play)]
        return guess
    #abbey
    else:
        guess = counter[RPS_game.abbey(prev_play)]
    opponent_history.append(prev_play)
    return guess

