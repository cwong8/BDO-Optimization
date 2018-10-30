# BDO-Optimization

This is a personal project of mine where I attempt to optimize the worker system in the online MMORPG Black Desert Online using Python. I had never used Python before this project so I learned a lot about the data analysis packets in Python (numpy, pandas) and the differences between Python and R (e.g. indexing starts at 0 for Python and 1 for R). Also, Jupyter Notebook allows me to easily share my code and results (when I get around to typing it up in Markdown) compared to R where I can use R Markdown (creates a PDF file) or R Shiny (requires a server).

The worker system consists of a map of main nodes and their subnodes that can be reached by connecting together nodes starting from a city. For a detailed map see: http://www.somethinglovely.net/bdo/.

## Main nodes
Each node in the game has a corresponding contribution point (CP) cost. Main nodes serve the purpose of connecting a player's network of nodes in-game. For example, players can connect a path between two cities to reduce the transportation cost of items between those two cities or giving themselves a route from one main node's trade material to the city. Within many main nodes are subnodes which contain resources that players can harvest using their worker empire.

## Subnodes
Subnodes serve as a way to passively gather materials while they "play" the game. They must be connected to from their main nodes and assigned workers to before they generate materials for the player.




