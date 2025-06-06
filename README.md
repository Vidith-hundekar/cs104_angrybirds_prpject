# Angrybirds(pygame-ce)

## CS-104 Project - Spring 2024-25

## Vidith Hundekar

---

## Outline

This report is about the game "Angry Birds" a 2Player game. It covers the game's instructions,implementation,game aspects,gameplay description,ideass ,references and the challenges encountered during development.

---

## Table of Contents

1. [Introduction to my Game](#introduction-to-my-game)
2. [Modules](#modules)
3. [Repo tree](#repo-tress)
4. [Instructions to run](#instructions-to-run)
   1. [Game Navigation ](#game-navigation)
5. [Gameplay description](#gameplay-description)
5. [Various Implementations in the Code](#various-implementations-in-the-code)
   1. [Customizations in the Game](#customizations-in-the-game)
6. [References](#references)

---

## Introduction to my Game

This is a 2Player game,each player tries to destroy oppenents fortress with their angry birds,first to do that with better accuray WINS.

---

## Modules

The external modules used are:

- `pygame-ce` - Version of pygame, Python module designed for writing code for  games.
- `Random` - A module that generates random number for various distributions.
- `Time` - A module that provides various time-related functions.
- `Math` - A module that provides many mathematical functions

---

## Repo tree

The project directory is as follows:

```
.
├── Modules
│   ├── MainMenu.py
│   ├── PlayGame.py
│   ├── Preferences.py
│   └── Scores.py
├── media
│   ├── fonts
│   ├── images
│   ├── sounds
│   └── videos
├── data
│   ├── path.txt
│   └── LeastTimes.txt
├── game.py
└── settings.py
```

- **`main.py`** - The main game loop.
- **`game.py`** - Contains all the global variables and modules necessary for the game to function smoothly.
- **`Modules`** - The programs that manage various game parts.
- **`media`** - Contains all the images, sounds, and fonts used in the game.
- **`data`** - Contains the path of the maze and the High ScoreCard (Least Time Taken).

---

## Instructions to run

### Game Navigation

Note: To ensure easy navigation between various screens, a back button is introduced which smoothly takes you to the previous screen.

#### Intro Screen

The game starts with an Intro Screen:

![Intro Screen](report/Intro.png)

#### Main Menu

After loading, you will be greeted with a Main Menu, from which you can choose to:

- Play
- See the Fastest Solves in each Level
- Customize the Game: Mute or Unmute
- Quit

You can select any of these by pressing on these buttons:

![Main Menu](report/MainMenu.png)

#### Game Level Selection

We have three levels of mazes from which you can choose:

![Game Level Selection](report/GameLevel.png)

#### Gameplay description

The game starts, waiting for you to navigate using the arrow keys or [W A S D]. The goal is to reach the door in the opposite corner. The _Score_ is measured in terms of the time taken to go to the opposite end: the Lower, the Better!

Various themes can be changed using the _Change Theme_ button. The music can be turned off by pressing the Music button.

Some examples of the game screens:

![Game Starts!](report/MazeGame.png)

![Game Play](report/MazeGameThemes.png)

#### Game Over

On reaching the opposite end, the game ends, and the time taken is displayed:

![Game Over](report/GameOver.png)

#### Fastest Solves

On clicking the Fastest Solves button on the Main Menu, you will see the Least Time taken to solve the various levels of the maze. An example screen:

![Fastest Solves](report/HighScores.png)

#### Preferences

This window enables you to mute the music part of the game. You can do this by clicking on the red music button. If you want the music back on, click the button again.

![Music On](report/PreferencesSoundOn.png)

![Music Off](report/PreferencesSoundOff.png)

#### Quit

On clicking this button, the game ends and the program terminates.

---

## Various Implementations in the Code

For the maze generation, I used the _Recursive Backtracking_ algorithm. This algorithm is a randomized version of the depth-first search algorithm. The algorithm starts at a random cell, chooses a random neighboring cell that has not been visited, creates a path between the two cells, and moves to the next cell. The algorithm continues until it has visited every cell in the grid. I have modified this algorithm slightly to make the wall size and the path size the same, which makes the maze look more appealing.

For the pathfinding, I used the A\* algorithm. The A\* algorithm is a pathfinding algorithm that uses a heuristic to determine the next node to visit in a graph. The algorithm uses a priority queue to determine the next node to visit based on the cost of the path to that node and the heuristic value of the node. The algorithm continues until it reaches the goal node or there are no more nodes to visit.

I have used the `heapq` module to implement the priority queue for the A\* algorithm.

For the pygame functions, I referred to the official documentation of pygame and pygame-ce, mostly the latter for the updated functions and methods.

---

### Customizations in the Game

A list of all the special customizations implemented in the game:

- Animation is when the player moves.
- Dynamic Background of the Main Menu.
- Music and Sound.
- Themes for the Game.
- High Scores.
- Preferences.
- Back Button for easy navigation.
- Customized Fonts.
- Responsive Buttons.

---

## References

1. [Pygame Official Documentation](https://www.pygame.org/docs/)
2. [Pygame CE Official Documentation](https://pyga.me/docs/)
3. [Maze Generation Algorithms by `professor-l`](https://professor-l.github.io/mazes/)
4. [A\* Algorithm](OtherResources/A*.md)

---
