from itinerary import Itinerary


class PathGenerator():
    '''
        PathGenerator class is used to generate an itinerary object
        from an edgeTo dictionary output by shortest path-finding algorithms.
    '''

    def __init__(self):
        '''
            Initialize a class instance
        '''
        self.allPath = []
        self.itineraries = []

    def dfs(self, edgeTo, current, start, visited, edges, connections):
        '''
            Use depth first search to extract all possible paths
        '''
        visited.append(current)

        for station in edgeTo[current]:
            # visit current's neighbors if they are unvisited
            if station[0] not in visited:
                # find corresponding connection using start,
                # end, and the line between them
                current_edge = next((connection for connection in connections
                                     if ((connection.s1 == station[0]
                                          and connection.s2 == current) or
                                         (connection.s2 == station[0]
                                          and connection.s1 == current)) and
                                     connection.line.id == station[1].id),
                                    None)
                if station[0].id == start.id:
                    self.allPath.append([current_edge] + edges)

                self.dfs(edgeTo, station[0], start, visited,
                         [current_edge] + edges, connections)
        # remove the current station so that
        # they can be visited by other possible paths
        visited.remove(current)
        if len(edges) > 0:
            edges.pop()

    def generatePath(self, edgeTo, start, end, connections):
        '''
            generate paths from edgeTo dictionary and convert
            them to itinerary objects
        '''
        self.dfs(edgeTo, end, start, [], [], connections)

        for path in self.allPath:
            self.itineraries.append(Itinerary(start, end, path))

        return self.itineraries

    def pickTopInitinerary(self):
        score_list = []
        for itinerary in self.itineraries:
            score_list.append(PathGenerator.calcPathScore(itinerary))
        i = score_list.index(min(score_list))

        return self.itineraries[i]

    def countStations(self):
        stations_used = set()
        for itinerary in self.itineraries:
            stations_used.add(itinerary.s1)
            stations_used.add(itinerary.s2)
        return len(stations_used)

    @staticmethod
    def calcPathScore(itinerary):
        score = itinerary.transfer_time + itinerary.travel_time
        return score

    @staticmethod
    def printAllPath(all_path):
        '''
            print all paths and their information
        '''
        for path in all_path:
            path.printItinerary()
