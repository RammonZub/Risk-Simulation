import threading
import random
from shared_resources import shared_lock  # Import the shared lock for thread safety

class Battle(threading.Thread):
    def __init__(self, attacker_territory, defender_territory, attacking_troops, current_player):
        super().__init__(daemon=True)
        self.attacker_territory = attacker_territory
        self.defender_territory = defender_territory
        self.attacking_troops = attacking_troops
        self.current_player = current_player
        self.winner = None
        self.lost_troops_attacker = 0
        self.lost_troops_defender = 0

    def run(self):
        try:
            attack_power = sum(random.randint(1, 6) for _ in range(self.attacking_troops))
            defense_power = sum(random.randint(1, 6) for _ in range(self.defender_territory.troops))

            if attack_power > defense_power:
                self.winner = self.current_player
                self.calculate_troops_lost(attacker_wins=True)
            else:
                self.winner = self.defender_territory.owner
                self.calculate_troops_lost(attacker_wins=False)

            with shared_lock:
                self.update_game_state()

            self.print_battle_outcome()

        except Exception as e:
            print(f"An error occurred during the battle: {e}")

    def calculate_troops_lost(self, attacker_wins):
        if attacker_wins:
            self.lost_troops_attacker = int(self.attacking_troops * 0.25)
            self.lost_troops_defender = self.defender_territory.troops
        else:
            self.lost_troops_attacker = self.attacking_troops
            self.lost_troops_defender = int(self.defender_territory.troops * 0.25)

    def update_game_state(self):
        self.attacker_territory.update_troops(-self.lost_troops_attacker)
        self.defender_territory.update_troops(-self.lost_troops_defender)

        if self.winner == self.current_player:
            self.transfer_territory_ownership()

    def transfer_territory_ownership(self):
        old_owner = self.defender_territory.owner
        self.defender_territory.set_owner(self.current_player)
        old_owner.territories.remove(self.defender_territory)
        self.current_player.territories.append(self.defender_territory)
        remaining_troops = max(1, self.attacking_troops - self.lost_troops_attacker)
        self.defender_territory.update_troops(remaining_troops)

    def print_battle_outcome(self):
        # Implement logic to print the battle outcome
        if self.winner == self.current_player:
            print(f"Battle won by {self.current_player.name}, successfully conquered {self.defender_territory.name}")
            print(f"- {self.current_player.name} lost {self.lost_troops_attacker} troops.")
            print(f"- {self.defender_territory.owner.name} lost {self.lost_troops_defender} troops.")
        else:
            print(f"Battle lost by {self.current_player.name}.{self.defender_territory.owner.name} won the battle.")
            print(f"{self.current_player.name} couldn't conquer {self.defender_territory.name}.")
            print(f"- {self.current_player.name} lost {self.lost_troops_attacker} troops.")
            print(f"- {self.defender_territory.owner.name} lost {self.lost_troops_defender} troops.")
        
        '''if self.winner:
            print(f"Battle won by {self.winner.name}.")
            if self.winner == self.current_player:
                print(f"{self.current_player.name} has successfully conquered {self.defender_territory.name}.")
                print(f"- {self.current_player.name} lost {self.lost_troops_attacker} troops.")
                print(f"- {self.defender_territory.owner.name} lost {self.lost_troops_defender} troops.")
            else:
                print(f"{self.current_player.name} didn't conquer {self.defender_territory.name}.")
                print(f"- {self.current_player.name} lost {self.lost_troops_attacker} troops.")
                print(f"- {self.defender_territory.owner.name} lost {self.lost_troops_defender} troops.")
        else:
            print(f"Battle lost by {self.current_player.name}.")
            print(f"- {self.current_player.name} lost all attacking troops.")'''

# You can add any additional methods or logic if needed








