from game import GameController, assign_territories_to_players, execute_reinforcement_phase
from board import Board, initialize_board
from player import Player
import random

if __name__ == "__main__":
    
  
    # Initialize AI Player
    players = [
        Player("alice"),
        Player("bob"),
        Player("jack"),

    ]

    board = initialize_board()

    # Set up the game controller with the players and the board
    game_controller = GameController(players, board)

    # Assign territories to players
    assign_territories_to_players(players, board.get_territories())

    # Execute the reinforcement phase
    execute_reinforcement_phase(players)

    # Start the game
    game_controller.start_game()

    # After the game is over
    #game_controller.end_game()

    
    

