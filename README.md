# Unity 3D AStar Algorithm Implementation

## Charles Anthony cc211002 Assignment2 for Unity

### About the project


### Get started

* Before running the project make sure you have unity3D installed on your machine.You can download it from Unity's official website.

### Project Structure

#### The project contains five main C# scripts that handle different aspects of the pathfinding algorithm

* Node.cs: This file defines the node class, which represents a cell in the 2d Grid.Each node knows its positionin the world, its position in the grid, whether its walkable, and its cost(gCost, hCost and fCost) that are used in the A* algorithm.

* Pathfinding.cs: This file contains the main pathfinding logic.it implements the a* algorithm, finding the best path from a start node to a target node. it also provides methods to calculate the distance between two nodes, to simplify the final path, and to etrace the path from the target node to the start node

* PathrequestManager.cs: This file handles requests for paths . it works with the pathfinding component to manage multiple path requests and prevents conficts.

* Unit.cs: This script is attached to the game units. it requests a path to the target then follows that path

* Grid.cs: This file defines a 2D grid of nodes, allowing the pathfinding algorithm to navigate through the world. it provides methods for getting a node from a point in the world, getting all neighbours of a node and so on

### How to Run

* Clone this repository to your local machine

* Select the repository from the browse-projects area and open it

* Select the play button to start the path finding algorithm from the seeker to the target

* The obstacles can be modified and the positions of the seeker and the target can also be changed as the user likes.



### Usage

* Once you hit play, the unit will finding a path to the target , avoiding any obstacles in between the path


### Further Related Development

* The scripts inside the folder provide a breakdown of the algorithm in detail. (Folder name: AStar_Breakdown).

* For the moment the languages they are written in are python and C. Some part of the file are still in progress.

* By creating a basic 2D grid ive tried to implement the grid, the functions taken, basic scanning of the grid to find the location of the target, a basic pathfinfing algorithm, the cost analysis of the entire path. These thing are implemented in the python files

* Running a python file. Commands are "python3 astar_breakdown.py" or if you have nodemon installed "nodemon --exec python3 astar_breakdown.py"

* Will be working on missing parts of the program that what the unity program already has.



### Contributing

* For the time being I am the sole contributor

### License

* This project is licensed under the MIT license. Free to use.

### Contact

Email -> cc211002@fhstp.ac.at \
Github -> https://github.com/charlesanthony1996 (project will be available there soon)

### Acknowledgements

Professor Hsiang-Yun Wu for her lectures and guidance
