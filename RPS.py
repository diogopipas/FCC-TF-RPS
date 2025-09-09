# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[]):

  if not prev_play:
    opponent_history.clear()
    
  opponent_history.append(prev_play)

  counter = {'R': 'P', 'P': 'S', 'S': 'R'}
  fallback_sequence = ["P", "S", "R"]

  num_plays = len(opponent_history) - 1

  if num_plays < 4:
    return fallback_sequence[num_plays % 3]
  
  prediction = None
  history = opponent_history[1:]

  for pattern_len in range(min(len(history) - 1, 10), 0, -1):
    last_sequence = history[-pattern_len:]

    next_move_counts = {'R': 0, 'P': 0, 'S': 0}

    for i in range(len(history) - pattern_len):
      if history[i:i + pattern_len] == last_sequence:
        next_move = history[i + pattern_len]
        next_move_counts[next_move] += 1
    
    if sum(next_move_counts.values()) > 0:
      # Predict the move that most frequently followed the pattern
      predicted_move = max(next_move_counts, key=next_move_counts.get)
      prediction = predicted_move
      break

  if prediction:
    my_move = counter[prediction]
  else:
    my_move = fallback_sequence[num_plays % 3]

  return my_move
