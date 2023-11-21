The board.py file in your project defines two main classes, Territory and Board, which together represent the game board and its individual territories. Here's a detailed breakdown of each class and its methods:

# Class: Territory
## Constructor __init__(self, name):

- Initializes a Territory instance with a given name.
- Sets initial values for owner, number of troops, and list of adjacent territories.
## Method set_owner(self, player):

- Sets the owner of the territory to a specified player.

## Method update_troops(self, number):

- Updates the number of troops in the territory.
- Ensures that the troop count does not fall below zero.

## Method add_adjacent_territory(self, territory, reciprocal=True):

- Adds an adjacent territory to the current territory.
- Ensures bidirectional adjacency without causing infinite recursion.

## Method is_adjacent(self, territory):

- Checks if a given territory is adjacent to the current one.

## Method add_troops(self, number):

- Adds a specified number of troops to the territory.

## Method __repr__(self):

- Provides a string representation of the Territory instance for debugging.

# Class: Board
## Constructor __init__(self):

- Initializes a Board instance with an empty dictionary of territories.

## Method add_territory(self, name):

- Adds a new territory to the board.
## Method set_adjacencies(self, territory_name, adjacencies):

- Sets the adjacent territories for a given territory.
## Method get_territories(self):

- Returns a shuffled list of all territories on the board.
## Method apply_random_event(self, event):

- Applies a random event to a territory with troops, reducing its troop count.
## Method __repr__(self):

- Provides a string representation of the Board instance.

# Additional Function: initialize_board()
- Initializes the game board with predefined territories and their adjacencies.

Main Block for Testing
Used to create an instance of the board, shuffle territories, and print them for testing purposes.
This structure allows for a dynamic representation of a game board, where territories can be added, their adjacencies defined, and random events applied. The Territory class provides a way to manage individual territories, including their owners, troop numbers, and relationships to other territories. The Board class manages the overall state of the game board, providing functions to manipulate and query its state. The setup of territories and adjacencies in the initialize_board function appears to be specific to a map of Colombia.
