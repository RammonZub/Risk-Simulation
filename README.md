
# Risk-Like Game Simulation

## Overview
This project is a simulation of a Risk-like strategy game, implemented in Python. It uses Object-Oriented Programming (OOP) principles and threading to simulate various aspects of the game, including territory control, battles, and player strategies.

### Key Features
- Thread-based simulation of battles.
- AI players making strategic decisions.
- Dynamic territory control system.

## Setup and Installation
Provide instructions on how to set up and run your project. Include any dependencies or prerequisites.


# Example of setup instructions
git clone https://github.com/your-github-username/your-repository-name.git
cd your-repository-name
python main.py

## Modules Documentation
Detailed documentation for each module can be found in the following links:
- [Battle Module](./BATTLE.md): Handles the battle simulation logic.
- [Board Module](./BOARD.md): Manages the game board and territories.
- [Game Module](./GAME.md): Controls the overall game flow and rules.
- [Player Module](./PLAYER.md): Defines the AI player behavior and actions.
- [Shared Resources](./SHARED_RESOURCES.md): Provides shared resources like locks for thread safety.


# Game Rules
## Territory Control
- Players begin the game by being assigned territories randomly.
- Each territory is initially populated with troops during the reinforcement phase. All players start with 30 troops
- Players can increase the number of troops in their territories through the placement phase.

## Battles and Conflict
- Battles occur when a player decides to attack an adjacent territory.
- The decision to attack is based on logic, primarily considering the difference in troop numbers between the attacking and defending territories.
- A battle is simulated in a separate thread using the Battle class.

## Troop Management
- Troops are lost or gained during battles and through random events.
- The number of troops in a territory can be updated through reinforcement, attack outcomes, or fortifications.
- Players can strategically move troops from one territory to another during the fortification phase.

## Winning and Losing Battles
- A battle's outcome is determined by comparing the combined attack power of the attacking troops against the defense power of the defending troops, both calculated using random dice rolls.
- The player with the higher total power wins the battle.
- The number of troops lost in battle is calculated as a proportion of the troops involved, depending on whether the attacker or defender wins.

## Gaining or Losing Territories
- If an attacker wins a battle, they gain control of the defending territory.
- The losing player loses control of the territory and the remaining troops in that territory.
- The victorious player moves their remaining troops into the newly conquered territory.

## Victory Conditions
- The game progresses in rounds, with each player taking turns to place troops, attack, and fortify.
- A player wins the game if they control all territories on the board.
- Alternatively, the game can end after a predetermined number of rounds, with the winner being the player controlling the most territories and troops.

## Additional Mechanics
- Random events can affect the number of troops in a territory, adding an element of unpredictability to the game.
- The game employs threading to simulate multiple battles and decisions concurrently, enhancing the dynamic nature of the simulation.
