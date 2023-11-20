import threading
import random


class GameController:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_player_index = 0
        self.game_over = False
        self.lock = threading.Lock()
        self.round_number = 1  # initialize the round counter

    # Keeps track of the current player, and increments the round number. 
    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        if self.current_player_index == 0:  # This means we wrapped around to the first player, in order to start the next round
            self.round_number += 1
            print(f"\nStarting Round {self.round_number}...")
            
            # Check for game over conditions
            if self.round_number > 50:
                self.game_over = True
                print(f"Round limit reached (Round {self.round_number - 1} was the last). Ending game...")
            elif any(len(player.territories) == len(self.board.territories) for player in self.players):
                winning_player = next(player.name for player in self.players if len(player.territories) == len(self.board.territories))
                self.game_over = True
                print(f"Player {winning_player} has conquered all territories. Ending game...")

                
                
                
                
    # Returns the current player
    def current_player(self):
        return self.players[self.current_player_index]
    
    # Triggers random events 
    def trigger_random_event_maybe(self):
        events = ['Storm', 'Meteorite', 'Rebellion']
        if random.randint(1, 4) == 1:  # 1 out of 4 chance of a random event happening
            event = random.choice(events)
            self.board.apply_random_event(event)


    # players actions in turn
    def execute_ai_turn(self, player):
        print(f"{player.name} is thinking...")
        
        # AI Logic for Placing Troops at the beggining of the game
        remaining_troops = sum(territory.troops for territory in player.territories)
        if remaining_troops > 0:
            player.place_troops(remaining_troops)

        # AI Logic for Attacking
        player.attack()

        # AI Logic for Fortification
        player.fortify()

    # Check if the player has territories, if not, they cannot play a turn (skips the round)
    def handle_no_territories(self, player):
        return not player.territories



    # Activities in a turn
    def play_turn(self):
        # Determine the current player
        player = self.current_player()
        print(f"\n{player.name} turn.")
        
        # Check if the player has territories, if not, skip the round
        if self.handle_no_territories(player):
            return

        # Trigger a random event 
        self.trigger_random_event_maybe()

        # Execute the turn using a new thread
        turn_thread = threading.Thread(target=self.execute_ai_turn, args=(player,))
        turn_thread.start()

        # Wait for the turn thread to finish before proceeding
        turn_thread.join()


    def start_game(self):
        print("Game has Started!")
        while not self.game_over:
            player = self.current_player()
            if player.territories:  # Player can only play if they have territories
                self.play_turn()
            '''else:
                print(f"{player.name} has no territories left and is skipped.")'''
            self.next_player()

        # End of game summary
        print("\n--- Ending State of the Game ---")
        # Winner determination based on most territories and troops
        winner = None
        max_territories = 0
        max_troops = 0

        for player in self.players:
            num_territories = len(player.territories)
            num_troops = sum(territory.troops for territory in player.territories)

            if num_territories > max_territories or (num_territories == max_territories and num_troops > max_troops):
                winner = player
                max_territories = num_territories
                max_troops = num_troops

        if winner:
            print(f"\nWinner based on most territories and troops: {winner.name} with {max_territories} territories and {max_troops} troops.")
        else:
            print("No winner could be determined.")
            
        
        for player in self.players:
            num_territories = len(player.territories)
            num_troops = sum(territory.troops for territory in player.territories)
            print(f"\nPlayer: {player.name}")

            if num_territories == 0:
                print("  Does not have any territories.")
            else:
                for territory in player.territories:
                    print(f"  Territory: {territory.name}, Troops: {territory.troops}")


#Assign territories to players
def assign_territories_to_players(players, territories):
    for player in players:
        if territories:  # Check if there are still territories to assign to players
            territory = territories.pop()
            territory.set_owner(player)
            player.add_territory(territory)
            print(f"{player.name} has been assigned {territory.name}")

    # Then distribute the rest of the territories randomly
    while territories:
        for player in players:
            if territories:  # Check if there are still territories to assign
                territory = territories.pop()
                territory.set_owner(player)
                player.add_territory(territory)
                print(f"{player.name} has been assigned {territory.name}")
            else:
                break

#Reinforcement phase, distribute a total of 30 troops randomly to the players territories, max 30 troops per player
def execute_reinforcement_phase(players):
    print(f"\n- - Reinforcement Phase - -")
    for player in players:
        remaining_troops = 30
        owned_territories = player.territories  # Get the territories owned by the player
        
        print(f"{player.name} starts distributing troops to their territories:")
        while remaining_troops > 0:
            chosen_territory = random.choice(owned_territories)  # Choose a territory at random
            troops_to_place = random.randint(1, remaining_troops)  # Decide how many troops to place
            chosen_territory.add_troops(troops_to_place)  # Add troops to the chosen territory
            remaining_troops -= troops_to_place  # Subtract the placed troops from the remaining count
            print(f" - {troops_to_place} troops added to {chosen_territory.name}, {remaining_troops} troops remaining")
    






