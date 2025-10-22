
## My Maze Localization Project Report

### Introduction

For this project, I made a program where an agent tries to find itself in a maze. It starts out lost, but it has a map of the whole maze. By moving and 'seeing' what's around it, it tries to figure out its exact spot.

My project uses a few Python files, each doing a specific job:
* **`maze.py`**: This file builds the maze.
* **`agent.py`**: This is where the agent's 'brain' is, helping it think about its location.
* **`gui.py`**: This file handles everything you see on the screen.
* **`main.py`**: This is the main file that starts and runs the whole program.

### How It Works

#### The Maze (`maze.py`)

* **Building the Maze:** I load the maze from a simple text file, like `example_maze.txt`. In this file, `1` means a wall, and `0` means an open path.
* **What the Agent Senses:** The `get_percept(x, y)` function in `maze.py` is important. It tells the agent what's directly around it (North, South, East, West). For example, if it sees `(1, 0, 1, 0)`, that means walls are North and East, and it's clear South and West.
* **Maze Borders:** I made sure that the outside edges of the maze act like walls too. This keeps things simple.

#### The Agent's Brain (`agent.py`)

This file holds the agent's 'brain' – how it keeps track of its location and learns more about it.

* **Starting Out Lost:** When the agent begins, it doesn't know its exact spot. So, it assumes it *could be* in any open space in the maze. I keep track of all these 'possible locations' in a list. This is like its starting idea of where it might be.
* **Learning by Eliminating:** Every time the agent moves and 'sees' something (gets a percept), it uses a clever trick to update its belief:
    * It looks at *every single possible spot* in the maze.
    * For each of these spots, it pretends it *started* there. Then, it replays all its past moves and what it *actually* saw.
    * If, at any point during this pretend journey, what it *would have seen* doesn't match what it *really saw*, then that starting spot is impossible. I remove it from the list of possible locations.
    * Only the spots that perfectly match *all* of its past experiences stay. This way, the agent gets smarter by ruling out wrong ideas.
* **Remembering the Past:** The agent also keeps a detailed record of its real moves and what it actually saw (`self.true_path_history`). This history is super important for the 'learning by eliminating' part.

#### What You See: The Screen (`gui.py`)

* **Possible Spots (Blue Squares):** On the screen, any place the agent might be is shown as a blue square. As the agent learns more, fewer blue squares should appear.
* **Agent's Real Spot (Red 'X'):** The agent's actual, secret location is always marked with a red 'X'. This is for me to see where it truly is.
* **Found It! (Green Border):** When the agent finally figures out its exact location, a green border appears around its real spot.

#### Running the Program (`main.py`)

* **Starting the Game:** This file sets up everything and starts the game.
* **Your Moves:** You can use the arrow keys to make the agent try to move.
* **Game Ends When:**
    * **Agent Finds Itself:** If the agent narrows down its possible spots to just one, it means it's found! The game stops.
    * **Too Many Steps:** I set a limit of 10 moves. If the agent hasn't found itself by then, the game also stops.

