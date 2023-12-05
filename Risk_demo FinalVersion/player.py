import random
import threading
from battle import Battle
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.territories = []  # Territories owned by the player
        self.decision_thread = None
        self.stop_event = threading.Event()

    def add_territory(self, territory):
        if territory not in self.territories:
            self.territories.append(territory)
            territory.set_owner(self)
            

    def place_troops(self, remaining_troops):
        if not self.territories:
            print(f"{self.name} has no territories to choose from.")
            return

        # AI logic for choosing a territory for placing troops
        chosen_territory = random.choice(self.territories)

        # AI logic for deciding the number of troops to place
        num_troops_to_place = min(random.randint(1, 5), remaining_troops)

        # Update troops in the chosen territory
        if chosen_territory in self.territories:
            chosen_territory.update_troops(num_troops_to_place)
            print(f"Placed {num_troops_to_place} troops in {chosen_territory.name}.")
        else:
            print(f"Error: {chosen_territory.name} is not owned by {self.name}")
            

    def attack(self):
        print(f"\n- - Attack Phase - -")
       
        # Choose the best target based on troop difference
        best_target = None
        max_troop_difference = -1
        for own_territory in [t for t in self.territories if t.troops > 1]:
            for adjacent_territory in own_territory.adjacent_territories:
                troop_difference = own_territory.troops - adjacent_territory.troops
                if troop_difference > max_troop_difference:
                    max_troop_difference = troop_difference
                    best_target = (own_territory, adjacent_territory)

        if not best_target:
            print(f"{self.name} has found no advantageous targets to attack.")
            return None  # No advantageous attack found

        from_territory, to_territory = best_target
        print(f"{self.name} has identified a target: Attacking {to_territory.name} from {from_territory.name}.")

        # Adjust logic for determining the number of troops
        if from_territory.troops == 2:
            num_troops = 1  # Only one troop can attack if there are two troops in the territory
        else:
            num_troops = random.randint(2, from_territory.troops - 1)  # Ensuring a valid attack

        print(f"{self.name} is attacking with {num_troops} troops.")

        # Execution of the attack
        battle = Battle(from_territory, to_territory, num_troops, self)  
        battle.start() # Start the battle as a thread
        battle.join()  # Wait for the battle to finish, enusre the thread is finished before proceeding
        #print(f"Battle initiated between {from_territory.name} and {to_territory.name}.")

        return battle



    def fortify(self):
        time.sleep(0.04)
        print(f"\n- - Fortification Phase - -")
        if not self.territories:
            print(f"{self.name} has no territories to fortify.")
            return

        # Find the weakest territory
        weakest_territory = min(self.territories, key=lambda t: t.troops)

        # Find an adjacent territory with more troops to transfer from
        source_territory = next((t for t in self.territories 
                                 if t.troops > weakest_territory.troops and t.is_adjacent(weakest_territory)), None)
        if not source_territory:
            print(f"{self.name} found no suitable territory to fortify from.")
            return  # No suitable source found

        # Transfer 50% of the troops from the source territory, minus one
        num_troops = max(1, (source_territory.troops // 2) - 1)
        
        if num_troops < source_territory.troops:
            source_territory.update_troops(-num_troops)
            weakest_territory.update_troops(num_troops)
            print(f"Moved {num_troops} troops from {source_territory.name} to {weakest_territory.name}.")
        else:
            print(f"{self.name} decides not to fortify any territories.")

        

    def start_turn(self):
        # Start a thread for AI decision-making
        self.stop_event.clear()
        self.decision_thread = threading.Thread(target=self.make_decision, daemon=True)
        self.decision_thread.start()

    def end_turn(self):
        # Stop the AI decision-making thread
        self.stop_event.set()
        if self.decision_thread:
            self.decision_thread.join(timeout=5)

    def __repr__(self):
        return f"Player(name={self.name})"
