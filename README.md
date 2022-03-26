# path-finders
A visualizer for path finding algorithms.

# Install and Run
- Download files.
- Download Python 3.x (if not already installed on your machine).
- Use a terminal to change directory to project root.
- In terminal run 'python main.py'

# How-To-Use
- In the start screen, press the associated letter that corresponds to the search algorithm you want to run.
- A screen with a grid/graph of light-green/open nodes appears (we will refer to the squares as nodes).
- In order to run the algorithm, at minimum, there must be a start state (blue node) and a goal state (gold node).
- You can also set higher cost nodes(nodes a darker shade of green) and walls (black nodes) that block the algorithm's search.
- You can press the space bar to run the algorithm.

## Setting the start state, goal state, and walls
- Begin by setting the start state (blue node) by left-clicking on a light green node. You can reset the start state by right-clicking the start state.
- Set the goal state (gold node) by left-clicking on a light green node. You can reset the goal state by right-clicking the goal state.
- Set walls (black nodes) by left-clicking on light green nodes. To make this function easier you can hold down the left mouse button and create walls in sequence.

## Setting higher cost nodes
- For algorithms such as A-Star Search and Uniform Cost Search, you can set the light-green nodes to have a higher cost. When setting nodes to have a higher cost, the shade of green will become darker. Light green is for low-cost nodes. Medium shade of green is for medium cost nodes. Dark shade of green is for high cost nodes.
- To create medium cost nodes, hold down the left-shift button and move the mouse over a node that is not a start/goal state or wall.
- To create high cost nodes, hold down the left-alt button and move the mouse over a node that is not a start/goal state or wall.

## Starting search
- Press the space bar to start the algorithm.
- The search agent's algorithm will search to find it's path.
- Then the search agent will walk the path.

## Restarting search algorithm
- At the very end of the visualization, press 'C' to restart the search algorithm.

## Search Algorithms Currently Supported
- Depth-First Search
- Breadth-First Search
- Iterative Deepening Depth First Search (Note: This algorithm is particularly slow for the provided visulaization since the graph has many nodes that form cycles. It is not recommended to have the start state and end state far from each other. The visualization will give you an idea of where the algorithm is searching)
- Uniform Cost Search
- A* Search
