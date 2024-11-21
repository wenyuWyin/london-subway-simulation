import heapq
import sys
from shortestPathAlgo import ShortestPathAlgo
from PrioritizedItem import PrioritizedItem


class Dijkstra(ShortestPathAlgo):

    def findShortestPath(self):
        '''
            Implementation of the Dijkstra algorithm
        '''
        edgeTo = {}
        distTo = {}
        pq = []

        expanding_count = 0

        # initialize distances from the starting station
        for station in self.s_list:
            distTo[station] = sys.maxsize
            edgeTo[station] = []
        distTo[self.start] = 0

        heapq.heappush(pq, PrioritizedItem(distTo[self.start], self.start))

        while pq:
            expanding_count += 1
            station = heapq.heappop(pq)
            # relax every edges(lines) adjacent to the current station
            out_edges = self.adjList.getOutEdges(station.item)

            for oe in out_edges:
                neighbor = oe[0]
                time = self.adjList.getTime(station.item, neighbor, oe[1])
                tentative_dist = distTo[station.item] + time
                # if current distance is less than previous distance,
                # update the distTo[neighbour] value
                if distTo[neighbor] > tentative_dist:
                    distTo[neighbor] = tentative_dist
                    # avoid duplicated items in edgeTo
                    if (station.item, oe[1]) not in edgeTo[neighbor]:
                        edgeTo[neighbor].append((station.item, oe[1]))
                    if neighbor in [item.item for item in pq]:
                        pq = ShortestPathAlgo.updatePQ(pq, neighbor,
                                                       distTo[neighbor])
                    else:
                        heapq.heappush(pq, PrioritizedItem(
                            distTo[neighbor],
                            neighbor))
        return edgeTo, expanding_count
