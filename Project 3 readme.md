# Text-Based Adventure Game

A simple Python-based text adventure game where the player navigates through a mysterious castle by making choices. The game includes different rooms, choices, and potential outcomes.

## Game Flow

### Game Start

```
Welcome to the Adventure Game!
You find yourself standing in front of a mysterious castle.
The air is cold, and the castle's gates creak in the wind.
You have two options:
1. Enter the castle
2. Walk around the castle
```

### If the player chooses to enter the castle:

```
You enter the castle. The inside is dark and musty.
There are two doors in front of you.
1. Go through the left door
2. Go through the right door
```

#### If the player chooses the left door:

```
You open the left door and enter a small room.
In the center of the room is a pedestal with a glowing gem on it.
Do you:
1. Take the gem
2. Leave the room
```

- If the player chooses to take the gem:

```
As you grab the gem, the floor beneath you collapses and you fall into a pit. Game Over!
```

- If the player chooses to leave the room:

```
You leave the room and head back to the main hallway.
```

#### If the player chooses the right door:

```
You open the right door and find a treasure chest in the corner of the room.
There are strange markings on the chest. Do you:
1. Open the chest
2. Leave the chest alone
```

- If the player chooses to open the chest:

```
Inside the chest, you find piles of gold and jewels! You win!
```

- If the player chooses to leave the chest alone:

```
You decide to leave the chest alone and return to the main hallway.
```

### If the player chooses to walk around the castle:

```
You walk around the castle but nothing interesting happens. Maybe you should try entering it?
```

## Requirements

- Python 3.x
- No additional libraries required

## How to Play

1. Clone this repository.
2. Run the `adventure_game.py` file in your local Python environment.
3. Make choices by entering the number corresponding to the option you want to select.

Enjoy the adventure!
``` 

This `README.md` contains the instructions, the flow of the game, and the expected output that the user will see based on their choices.
