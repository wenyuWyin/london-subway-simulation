from sys import maxsize
from itertools import permutations


class TSP():
    '''
        TSP class implements the brute-force algorithm
        to find the most efficient route for a patrol
        to visit all required stations.
        Inputs: adjList -
                    AdjList object that represents the entire graph
                start -
                    Station object that represents where the officer starts at
                patrol_stations -
                    A list of stations objects that describes the stations
                    that the officer needs to visit
    '''

    def __init__(self, adjList, start, patrol_stations):
        '''
            Initialize a class instance
        '''
        self.adjList = adjList
        self.start_s = start
        self.patrol_s = patrol_stations

        self.min_path = maxsize
        self.shortest_path = []

    # Note the line numbers of connections in this function do not
    # matter since all lines between two stations take the exact
    # same time.
    def travellingSalesmanProblem(self):
        '''
            Implement the brute-force algorithm
            (generate all possible paths and calculate cost of each)
        '''
        # store all vertex apart from the starting vertex
        self.patrol_s.remove(self.start_s)

        # store minimum weight Hamiltonian Cycle
        next_permutation = permutations(self.patrol_s)
        for perm in next_permutation:
            # initialize current Path weight(cost)
            current_pathweight = 0
            path_exist = True

            # compute current path weight
            currentS = self.start_s
            for nextS in perm:
                try:
                    time = self.adjList.getAllTime(currentS, nextS)
                    current_pathweight += time
                except KeyError:
                    # set path_exist to false if one of the
                    # connections does not exist
                    path_exist = False
                    break
                currentS = nextS
            try:
                time = self.adjList.getAllTime(currentS, self.start_s)
                current_pathweight += time
            except KeyError:
                path_exist = False

            # update minimum
            if path_exist:
                if self.min_path != min(self.min_path, current_pathweight):
                    self.shortest_path = perm
                self.min_path = min(self.min_path, current_pathweight)

    def printShortestPath(self):
        '''
            Print the solution to the patrolling problem
        '''
        print(f'{self.start_s.id} -> ', end='')
        for s in self.shortest_path:
            if self.shortest_path.index(s) != len(self.shortest_path) - 1:
                print(f'{s.id} -> ', end='')
            else:
                print(f'{s.id} -> {self.start_s.id}')
