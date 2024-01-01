# Text Adventure Game

This is a simple text-based adventure game implemented in Python. The player is presented with a series of choices and has to navigate through a cave by making the correct decisions.

## Gameplay

The game starts with the player outside a mysterious cave. The player can choose to enter the cave or not.

If they enter, they have to explore the cave by choosing between different paths. Choosing the wrong path will lead to failure. 

At certain points, the player will find treasures and keys that unlock new areas and progress the story.

The goal is to successfully navigate through the cave by making the right choices when presented with options. Reaching the end wins the game.

## Code Overview

- `introduction()` displays the opening text
- `make_choice()` gets player input
- Different functions represent different parts and paths in the cave
- Player choices determine the path through the game
- Wrong choices lead to `game_over()`
- Reaching `enter_portal()` wins the game

The code is structured as a linear sequence of functions that model the narrative. Player choices steer execution flow through the functions.

## How to Play

Run `python text_based_game.py` to start the game. Follow the prompts and make choices to progress the story.

Try to reach the end by always making the right decisions when given an option.

## Future Improvements

- Add more choices and branching paths
- Implement inventory system
- Add NPC characters
- Improve parser for handling more input varieties
- Expand the world and story

## Disclaimer

This game was built for educational purposes and represents a very simple version of a text adventure game. Significant effort is required to turn it into a full-fledged adventure game.

Suggestions for improvements are welcome!
