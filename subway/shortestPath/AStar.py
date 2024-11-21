import math
import heapq
import sys
from shortestPathAlgo import ShortestPathAlgo
from PrioritizedItem import PrioritizedItem


class Astar(ShortestPathAlgo):

    @staticmethod
    def __h(current, end):
        '''
            heuristic function return the distance from current
            station to the destination
        '''
        return math.sqrt(math.pow(current.lat - end.lat, 2) +
                         math.pow(current.lon - end.lon, 2)) * 192.127

    def findShortestPath(self):
        '''
            Implementation of the A* algorithm with the help of
            the heuristic function defined above
        '''
        edgeTo = {}
        distTo = {}
        totalCost = {}

        pq = []

        expanding_count = 0

        # initialize distance and total cost from starting station
        for station in self.s_list:
            distTo[station] = sys.maxsize
            totalCost[station] = sys.maxsize
            edgeTo[station] = []
        distTo[self.start] = 0
        totalCost[self.start] = 0

        heapq.heappush(pq, PrioritizedItem(totalCost[self.start], self.start))

        while pq:
            expanding_count += 1
            station = heapq.heappop(pq)

            # print(f'exploring {station.item.id}')

            if station.item.id == self.end.id:
                return edgeTo, expanding_count

            # relax all edges connected to the current station
            out_edges = self.adjList.getOutEdges(station.item)

            for oe in out_edges:
                neighbor = oe[0]
                time = self.adjList.getTime(station.item, neighbor, oe[1])
                tentative_dist = distTo[station.item] + time
                # if the new distance to neighbor is shorter than the distance
                # stored before, update distTo, edgeTo, totalCost, and the
                # priority queue
                if distTo[neighbor] > tentative_dist:
                    distTo[neighbor] = tentative_dist
                    h_result = Astar.__h(neighbor, self.end)
                    totalCost[neighbor] = tentative_dist + h_result
                    # avoid duplicated items in edgeTo
                    edgeTo[neighbor] = [(station.item, oe[1])]
                    if neighbor in [item.item for item in pq]:
                        pq = ShortestPathAlgo.updatePQ(pq, neighbor,
                                                       distTo[neighbor])
                    else:
                        heapq.heappush(pq, PrioritizedItem(totalCost[neighbor],
                                                           neighbor))

        return edgeTo, expanding_count
