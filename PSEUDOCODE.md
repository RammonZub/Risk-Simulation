
// ai.pseudo
Class AI Inherits Player:
  Initialize AI:
    - Call parent class initializer with name and AI status
    - Create a decision thread placeholder
    - Create an event to stop the decision process

  Function choose_territory_for_troops:
    - Selects a random territory from the AI's territories to place troops
    - If AI has no territories, return None

  Function decide_troops_to_place:
    - Decides a random number of troops to place, up to a maximum or remaining troops

  Function decide_attack:
    - Determines if there is a valid attack move from AI's territories
    - Selects a random territory to attack from and to, and the number of troops to use

  Function calculate_troops_to_fortify:
    - Randomly calculates troops to move from one territory to another for fortification

  Function decide_fortify:
    - Decides if fortification should take place
    - Randomly chooses territories to fortify from and to, and number of troops to move

  Function start_turn:
    - Clears the stop event
    - Starts the decision thread

  Function end_turn:
    - Sets the stop event
    - Waits for the decision thread to finish

// Battle.pseudo
Class Battle Inherits Thread:
  Initialize Battle:
    - Initializes with attacker and defender territories, attacking troops, and a lock
    - Sets the winner and lost troops counters to None

  Function run:
    - Simulates the battle when the thread starts
    - Determines the attack and defense power
    - Calculates lost troops for attacker and defender
    - Updates troops and ownership of territories accordingly
    - Handles exceptions if they occur

// board.pseudo
Class Territory:
  Initialize Territory:
    - Sets the territory's name, owner, troops, and adjacent territories

  Function set_owner:
    - Assigns a player as the owner of the territory

  Function update_troops:
    - Updates the number of troops in the territory, ensuring it doesn't go negative

  Function add_adjacent_territory:
    - Adds an adjacent territory, and optionally adds this territory as adjacent to the other

  Function is_adjacent:
    - Checks if a territory is adjacent

  Function add_troops:
    - Adds troops to the territory


Class Board:
  Initialize Board:
    - Creates a dictionary to hold territories

  Function add_territory:
    - Adds a territory with the given name to the board

  Function set_adjacencies:
    - Sets adjacent territories for a given territory

  Function get_territories:
    - Returns a list of all territories on the board


// GameController.pseudo

Class GameController
  Description: Manages the game state, player turns, and the overall flow of the game.

  Constants:
    MAX_ROUNDS = 100

  Properties:
    players: List of Player objects participating in the game.
    board: The game board with all territories.
    thread_manager: Manages threads, specifically battles.
    active_player_index: Index of the currently active player.
    game_over: Boolean flag for whether the game is over.
    lock: Thread lock to manage synchronization.
    round_number: Counter for the number of rounds that have been played.

  Methods:
    Constructor(players, board, thread_manager)
      Initializes a new GameController instance.

    next_player()
      Advances the active player index and increments round_number if needed.

    current_player()
      Returns the current active player.

    play_turn()
      Facilitates a single turn for the active player. Handles AI and human players differently.

    check_for_draw_or_winner_by_territories()
      Checks if the game should end in a draw or if there is a winner by territory control.

    start_game()
      Begins the game loop and continues until a terminal condition is reached.

    end_game()
      Finalizes the game, displaying ending messages and any cleanup needed.

// main.pseudo

Main Execution Block
  Description: Sets up and starts the game by initializing components and players.

  Steps:
    - Initialize the game board and territories.
    - Create Player and AI objects.
    - Shuffle and assign territories to players.
    - Distribute initial troops among player territories.
    - Initialize the game controller with players, board, and thread manager.
    - Start the game using the game controller.
    - End the game once finished.

// Player.pseudo

Class Player
  Description: Represents a player in the game, capable of managing territories and troops.

  Properties:
    name: The player's name.
    is_ai: Boolean indicating if the player is an AI.
    territories: List of territories owned by the player.

  Methods:
    Constructor(name, is_ai)
      Initializes a new player with a given name and AI status.

    place_troops(territory, num_troops)
      Places troops on a specified territory.

    attack(from_territory, to_territory, num_troops)
      Conducts an attack from one territory to another.

    fortify(from_territory, to_territory, num_troops)
      Moves troops between owned territories to strengthen a position.

    add_territory(territory)
      Adds a territory to the player's control.

    get_territories()
      Returns a list of territories owned by the player.

// ThreadManager.pseudo

Class ThreadManager
  Description: Handles the creation and resolution of battle threads.

  Properties:
    battle_threads: A list of threads that are handling ongoing battles.
    lock: A reentrant lock to ensure thread-safe operations.

  Methods:
    Constructor()
      Initializes a new instance of ThreadManager.

    create_battle(attacker_territory, defender_territory, attacking_troops)
      Starts a new battle in a separate thread.

    initiate_battle(attacker_territory, defender_territory, attacking_troops)
      Handles the logic to start a battle without threading.

    resolve_battles()
      Waits for all battle threads to finish and clears completed threads.

    manage_ai(ai_player)
      Manages the actions of an AI player within a separate thread.

    synchronize_ai(ai_player)
      Synchronizes after an AI player's turn has ended.
