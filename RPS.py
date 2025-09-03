# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[]):
  """
  This player bot uses a historical pattern matching strategy to predict the opponent's next move.
  It works by:
  1. Storing the opponent's move history.
  2. Identifying the opponent's most recent sequence of moves (the "pattern").
  3. Searching the history for all previous times this pattern occurred.
  4. Analyzing what move the opponent made immediately after the pattern in the past.
  5. Predicting the opponent's next move will be the one that most frequently followed the pattern.
  6. Playing the counter-move to the prediction.
  """

  # On the first turn of a match, prev_play is empty. This is a good time to clear
  # the history from any previous matches.
  if not prev_play:
    opponent_history.clear()
    
  opponent_history.append(prev_play)

  # Define the winning moves and a fallback sequence for the start of the game
  counter = {'R': 'P', 'P': 'S', 'S': 'R'}
  fallback_sequence = ["P", "S", "R"]

  # The actual number of moves we have in our history (ignoring the initial empty string)
  num_plays = len(opponent_history) - 1

  # For the first few moves, we don't have enough data, so we use the fallback
  if num_plays < 4:
    return fallback_sequence[num_plays % 3]

  # --- Pattern Matching Logic ---
  
  prediction = None
  
  # The history we'll search (we don't need the initial empty string)
  history = opponent_history[1:]

  # We will search for patterns of decreasing length. The most specific (longest)
  # pattern that has occurred before is the best one to use for prediction.
  # We cap the max length to 10 to keep it efficient.
  for pattern_len in range(min(len(history) - 1, 10), 0, -1):
    # The pattern is the most recent sequence of opponent moves
    last_sequence = history[-pattern_len:]

    # Count what move the opponent played *after* this sequence occurred in the past
    next_move_counts = {'R': 0, 'P': 0, 'S': 0}

    # Search the entire history for previous occurrences of this sequence
    for i in range(len(history) - pattern_len):
      if history[i:i + pattern_len] == last_sequence:
        next_move = history[i + pattern_len]
        next_move_counts[next_move] += 1
    
    # If we found at least one match, we can make a prediction
    if sum(next_move_counts.values()) > 0:
      # Predict the move that most frequently followed the pattern
      predicted_move = max(next_move_counts, key=next_move_counts.get)
      prediction = predicted_move
      # Once we've found a prediction with the longest possible pattern, we stop.
      break

  # --- Determine Our Move ---

  if prediction:
    # If we have a prediction, play the move that beats it
    my_move = counter[prediction]
  else:
    # If no patterns were found (very unlikely), use the fallback
    my_move = fallback_sequence[num_plays % 3]

  return my_move