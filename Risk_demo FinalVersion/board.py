
import random

class Territory:
    def __init__(self, name):
        self.name = name
        self.owner = None
        self.troops = 0
        self.adjacent_territories = []

    def set_owner(self, player):
        self.owner = player

    def update_troops(self, number):
        self.troops += number
        if self.troops < 0:
            self.troops = 0

    def add_adjacent_territory(self, territory, reciprocal=True):
        if territory not in self.adjacent_territories:
            self.adjacent_territories.append(territory)
            if reciprocal:  # Prevent recursion by using a flag
                territory.add_adjacent_territory(self, reciprocal=False)

    def is_adjacent(self, territory):
        return territory in self.adjacent_territories
    
    def add_troops(self, number):
        self.troops += number

    def __repr__(self):
        return f"Territory(name={self.name}, owner={self.owner}, troops={self.troops})"



class Board:
    def __init__(self):
        self.territories = {}

    def add_territory(self, name):
        if name not in self.territories:
            territory = Territory(name)
            self.territories[name] = territory

    def set_adjacencies(self, territory_name, adjacencies):
        if territory_name in self.territories:
            for adj in adjacencies:
                if adj in self.territories:
                    self.territories[territory_name].add_adjacent_territory(self.territories[adj])

    def get_territories(self):
        territories_list = list(self.territories.values())
        random.shuffle(territories_list)
        return territories_list

    def apply_random_event(self, event):
        # Filter territories that have troops
        territories_with_troops = [t for t in self.territories.values() if t.troops > 0]

        # Proceed only if there are territories with troops
        if territories_with_troops:
            affected_territory = random.choice(territories_with_troops)

            # Ensure the reduction is at least 10% and at most 60%
            reduction_percentage = random.randint(10, 60)
            troops_to_remove = max(1, int(affected_territory.troops * (reduction_percentage / 100.0)))

            affected_territory.troops -= troops_to_remove
            print(f"A {event} occurred in {affected_territory.name} and lost {troops_to_remove} troops.")
        else:
            print("No territories with troops to affect.")


    def __repr__(self):
        return '\n'.join(str(territory) for territory in self.territories.values())

            
# Adding Colombia territories 
def initialize_board():
    board = Board()
    european_countries = ['France', 'Germany', 'Italy', 'Spain', 'United Kingdom']
    for country_name in european_countries:
        board.add_territory(country_name)

    # Set adjacencies 
    board.set_adjacencies('France', ['Germany', 'Spain'])
    board.set_adjacencies('Germany', ['France', 'Italy'])
    board.set_adjacencies('Italy', ['Germany', 'Spain', 'United Kingdom'])
    board.set_adjacencies('Spain', ['France', 'Italy'])
    board.set_adjacencies('United Kingdom', ['Italy'])

    return board


# Testing purposes only.
if __name__ == '__main__':
    board = initialize_board()  # Corrected function call
    territories = board.get_territories()
    # Print all territories
    print(board)
    print(f"Territories before shuffling (Type: {type(territories)}): {territories}")
    random.shuffle(territories)
    print("Territories after shuffling:", territories)

