The game.py file defines the GameController class and two functions, assign_territories_to_players and execute_reinforcement_phase, which together control the gameplay and logic of the game.

#Class: GameController
## Constructor __init__(self, players, board):

- Initializes a game with the given players and board.
- Sets the initial player index, game state, a lock for thread safety, and the round number.
## Method next_player(self):

- Advances to the next player and increments the round number.
- Checks for game-over conditions, either by round limit or a player controlling all territories.
## Method current_player(self):

- Returns the current player based on the player index.
## Method trigger_random_event_maybe(self):

- Randomly decides whether to trigger a random event on the board.
## Method execute_ai_turn(self, player):

- Executes a turn for the AI player, including placing troops, attacking, and fortification.
## Method handle_no_territories(self, player):

- Checks if a player has any territories. If not, their turn is skipped.
## Method play_turn(self):

- Orchestrates a player's turn, including triggering random events and executing AI logic in a separate thread.
## Method start_game(self):

- Begins the game loop, processing turns until the game is over.
- Determines and announces the winner based on territories and troops.
# Function: assign_territories_to_players(players, territories)
- Assigns territories to players, ensuring each player gets an equal starting position.
- Distributes the remaining territories randomly among players.
# Function: execute_reinforcement_phase(players)
- Distributes a set number of troops (30 per player) among the player's territories.
- Ensures that troops are distributed randomly across each player's territories.
# Gameplay Flow
- The GameController class manages the flow of the game, including player turns, AI actions, and checking for game-over conditions.
- The assign_territories_to_players function sets the initial territory ownership at the start of the game.
- The execute_reinforcement_phase function allows players to reinforce their territories with additional troops at the beginning of the game.


