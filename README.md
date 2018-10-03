# BDO-Optimization

This is a personal project of mine where I attempt to optimize the worker system in the online MMORPG Black Desert Online using Python. I had never used Python before this project so I learned a lot about the data analysis packets in Python (numpy, pandas) and the differences between Python and R (e.g. indexing starts at 0 for Python and 1 for R). Also, Jupyter Notebook allows me to easily share my code and results (when I get around to typing it up in Markdown) compared to R where I can use R Markdown (creates a PDF file) or R Shiny (requires a server).

The worker system consists of a map of main nodes and their subnodes that can be reached by connecting together nodes starting from a city. For a detailed map see: http://www.somethinglovely.net/bdo/.

## Main nodes
Each node in the game has a corresponding contribution point (CP) cost. Main nodes serve the purpose of connecting a player's network of nodes in-game. For example, players can connect a path between two cities to reduce the transportation cost of items between those two cities or giving themselves a route from one main node's trade material to the city. Within many main nodes are subnodes which contain resources that players can harvest using their worker empire.

## Subnodes
Subnodes serve as a way to passively gather materials while they "play" the game. They must be connected to from their main nodes and assigned workers to before they generate materials for the player.

## 

### State of BDO / My experience with the game
To progress at any decent rate within the game requires the players to leave their computers on for absurd amounts of time (i.e. overnight, while they go to work) so their in-game workers continue to gather materials. Basically, this means that the game becomes a second "job" for most of its serious players. These are the players that you will see in the towns processing raw materials for hours everyday while they are away from their computers (AFK). Korean MMORPGs are notorious for having extreme grinding (performing repetitive tasks for gameplay advantage) in the end-game. The enhancement system is notorious for deleting months of progress in seconds once players progress past the soft-cap (+18 or TRI gear). As such, the developers add in cash-shop items to alleviate this grind in which players can choose to spend real money to gain an advantage in the game. This is what players call "pay-to-win" because those with disposable income can progress faster than players who do not spend money in the game (and don't get me started on value packs). I quit this game back in April-May 2017 because it became more of a job than a game but the worker system has always intrigued me which is why I attempt to use the skills I have to find some solution.


