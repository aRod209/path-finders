# path-finders
A visualizer for path finding algorithms.

# Install and Run
- Download files.
- Download Python 3.x (if not already installed on your machine).
- Use a terminal to change directory to project root.
- In terminal run 'python main.py'

# How-To-Use
- In the start screen, press the associated letter that corresponds to the search algorithm you want to run.
- A screen with a grid of light-green/open nodes appears (we will refer to the squares as nodes).
- In order to run the algorithm, at minimum, there must be a start state (blue node) and a goal state (gold node).
- You can also set higher cost nodes(nodes a darker shade of green) and walls (black nodes) that block the algorithm's search.
- You can press the space bar to run the algorithm.

## Setting the start state, goal state, and walls
- Begin by setting the start state (blue node) by left-clicking on a light green node.
- Set the goal state (gold node) by left-clicking on a light green node.
- Set walls (black nodes) by left-clicking on light green nodes. To make this function easier you can hold down the left mouse button and create walls in sequence.

## Setting higher cost nodes
- For algorithms such as A-Star Search and Uniform Cost Search, you can set the open/light-green nodes to have a higher cost. When setting nodes to have a higher cost, the shade of green will become darker. Light green is for low-cost nodes. Medium shade of green is for medium cost nodes. Dark shade of green is for high cost nodes.
- To create medium cost nodes, hold down the left-shift button and the left mouse button over an open node.
- To create high cost nodes, hold down the left-alt button and the left mouse button over an open node.

## Starting search
- Press the space bar to start the algorithm.
- The search agent's algorithm will search to find it's path.
- Then the search agent will walk the path.

## Restarting search algorithm
- At any time you can Press 'C' to restart the search algorithm.
