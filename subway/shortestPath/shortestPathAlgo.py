import heapq
from PrioritizedItem import PrioritizedItem
from pathGenerator import PathGenerator


class ShortestPathAlgo():
    '''
        Abstract class for path finding algorithms
    '''

    def __init__(self, adj_list, s_list, c_list, start_s, end_s):
        '''
            Initialize a class instance
        '''
        self.adjList = adj_list
        self.s_list = s_list
        self.c_list = c_list
        self.start = start_s
        self.end = end_s

    def findShortestPath():
        pass

    def runAlgorithm(self):
        '''
            Run Dijkstra or A* to find shortest paths
            Output: A list of possible paths
        '''
        path_gen = PathGenerator()
        edgeTo, _ = self.findShortestPath()
        paths = path_gen.generatePath(edgeTo, self.start,
                                      self.end, self.c_list)
        return paths

    @staticmethod
    def updatePQ(pq, station, new_priority):
        prioritizedItem = next((i for i in pq if i.item == station), None)
        pq.remove(prioritizedItem)
        heapq.heappush(pq, PrioritizedItem(new_priority, station))
        return pq
