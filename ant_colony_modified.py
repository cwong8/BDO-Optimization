import random as rn
import numpy as np
from numpy.random import choice as np_choice

class AntColony(object):

    def __init__(self, distances, start_node, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        Args:
            distances (2D numpy.array): Square matrix of distances. Diagonal is assumed to be np.inf.
            start_node: Index of node to start paths from
            n_ants (int): Number of ants running per iteration
            n_best (int): Number of best ants who deposit pheromone
            n_iteration (int): Number of iterations
            decay (float): Rate it which pheromone decays. The pheromone value is multiplied by decay, so 0.95 will lead to decay, 0.5 to much faster decay.
            alpha (int or float): exponenet on pheromone, higher alpha gives pheromone more weight. Default=1
            beta (int or float): exponent on distance, higher beta give distance more weight. Default=1

        Example:
            ant_colony = AntColony(german_distances, 100, 20, 2000, 0.95, alpha=1, beta=2)          
        """
        self.distances  = distances
        # Added start_node
        self.start_node = start_node
        self.pheromone = np.ones(self.distances.shape) / len(self.distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        
        # Added start_connections
        # Start connections is an array of all nodes connected to the starting node (excluding itself)
        self.start_node_row = distances[self.start_node, :]
        self.start_connections_array = np.where(np.isinf(self.start_node_row) == False)
        self.start_connections = set()  
        for x in self.start_connections_array[0]: self.start_connections.add(x)

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            #print (shortest_path)
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone * self.decay  
        # Return output of visited nodes to copy into node_name
        return all_time_shortest_path

    def spread_pheronome(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                # End of path check
                if (move == 'End of path'): return
                self.pheromone[move] += 1.0 / self.distances[move]
    """
    # Replaced by gen_avg_path_dist
    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            # End of path exception and makes sure the last valid element in path does not add np.inf to our distance
            if (ele == 'End of path' or self.distances[ele] == np.inf): return total_dist
            total_dist += self.distances[ele]
        return total_dist
    """

    def gen_avg_path_dist(self, path):
        total_dist = 0
        for ele in path:
            # End of path exception and makes sure the last valid element in path does not add np.inf to our distance
            if (ele == 'End of path' or self.distances[ele] == np.inf): return total_dist / (len(path)-1)
            total_dist += self.distances[ele]
        # Add average distance to measure best routes:
        # A path of length 3 going to 3 main nodes is worse than a path of length 4 going into a subnode
        return total_dist / (len(path)-1)

    
    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(self.start_node)
            all_paths.append((path, self.gen_avg_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        # Changing visited to a local variable within AntColony instead of local in only gen_path
        # This lets us call visited in run(self) with node_name to get all nodes visited
        self.visited = set()
        self.visited.add(start)
        prev = start
        #for i in range(len(self.distances) - 1):
        while ((self.visited & self.start_connections) != self.start_connections):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], self.visited)
            path.append((prev, move))
            prev = move
            self.visited.add(move)
            # Stop finding a path when reaching an End of path
            # self.distances[prev, move] == np.inf
            if (move == self.start_node):
                path.append('End of path')
                prev = move
        return path
        path.append((prev, start)) # going back to where we started    

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        # Sets pheromone of visited nodes to zero so the ants do not go backwards
        pheromone[list(visited)] = 0
        
        # Careful with alpha and beta values. Large exponents may cause overflow or underflow (i.e. e+16 == inf and e-16 == 0)
        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)
        # Ensures that we return to start_node after reaching an End of path
        if (row.sum() == 0):
            move = self.start_node
            return move
        norm_row = row / row.sum()
        # This returns 0 if all probabilities are zero (i.e. no more places to go)
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move

