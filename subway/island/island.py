from AStar import Astar
import sys


class Island:
    '''
        Island class identify various zones in the subway system,
        categorizes stations according to the islands they are in,
        and finds connections between two islands given two stations.
    '''

    def __init__(self, stations, connections, adjList):
        '''
            Initialize a class instance
        '''
        self.s_list = stations
        self.c_list = connections
        self.adjList = adjList

        self.zone_graph = {}
        # {zone: [[s1, s2], [s3]], zone: [[s4, s5, s6], [s7, s8], [s9]]}
        self.island_graph = {}

        for s in self.s_list:
            if s.zone % 1 == 0:
                self.__initZoneGraph(int(s.zone), s)
            else:
                self.__initZoneGraph(int(s.zone+0.5), s)
                self.__initZoneGraph(int(s.zone-0.5), s)

    def __initZoneGraph(self, zone_num, station):
        '''
            Categorize a station into its correct zone_num list
        '''
        if zone_num in self.zone_graph:
            self.zone_graph[zone_num].append(station)
        else:
            self.zone_graph[zone_num] = [station]
            self.island_graph[zone_num] = []

    def separateIslandInZone(self):
        '''
            Run DFS in each zone to identify islands
        '''
        for zone, stations in self.zone_graph.items():
            visited = []
            for station in stations:
                island = []
                if station not in visited:
                    island = self.DFS(island, station, visited, zone)
                    self.island_graph[zone].append(island)

    def DFS(self, temp, current, visited, zone):
        '''
            DFS algorithm to search for islands
        '''
        visited.append(current)
        temp.append(current)

        # Run DFS at every station
        for oe in self.adjList.getOutEdges(current):
            if oe[0] in self.zone_graph[zone]:
                if oe[0] not in visited:
                    temp = self.DFS(temp, oe[0], visited, zone)
        return temp

    def printIsland(self):
        '''
            Print out all islands in a graph
        '''
        for zone, islands in self.island_graph.items():
            print(f'\nIn zone{zone}, the islands are the following: ')
            for i, island in enumerate(islands):
                print('--------------------------')
                print(f"Island{i+1} contains station(s): ", end="")
                for station in island:
                    if island.index(station) != len(island)-1:
                        if island.index(station) != len(island)-1:
                            print(station.id, end=", ")
                        else:
                            print(station.id)
                    else:
                        print(station.id)

    def __findIslandUtils(self, s, zone):
        '''
            Find the island that an island belongs to
            given a specific zone that the island is in
        '''
        for island in self.island_graph[zone]:
            if s in island:
                return [island]

    def __findAllIsland(self, s):
        '''
            Find all islands that one station belongs to
            (could be either 1 island or 2 islands)
        '''
        if s.zone % 1 == 0:
            # iterate through all islands in the corresponding zone
            # to find where island the station belongs to
            return self.__findIslandUtils(s, s.zone)
        else:
            island1 = self.__findIslandUtils(s, s.zone+0.5)
            island2 = self.__findIslandUtils(s, s.zone-0.5)
            return island1 + island2

    def __findIslandConnectionUtils(self, islands1, islands2):
        '''
            Find the connection between two islands
        '''
        shortest_dist = sys.maxsize
        for s1 in islands1:
            for s2 in islands2:
                # Run A* at every two stations to find the shortest
                # path between the two islands
                algo = Astar(self.adjList, self.s_list, self.c_list, s1, s2)
                paths = algo.runAlgorithm()
                # Update shortest distance and shortest path
                if paths[0].travel_time < shortest_dist:
                    shortest_connection = paths[0]
                    shortest_dist = paths[0].travel_time
        print()
        shortest_connection.printItinerary(extra_info=False, zone_info=True)
        return shortest_connection

    def findIslandConnection(self, *args):
        '''
            Find the connection between two islands.
            In the case of four islands
            (s1.zone = s2.zone = n+0.5 where n is an integer),
            the function only outputs connections
            between islands in the same zone.
        '''
        if len(args) <= 2:
            return self.__findIslandConnectionUtils(args[0], args[1])
        else:
            return (self.__findIslandConnectionUtils(args[0], args[1]),
                    self.__findIslandConnectionUtils(args[2], args[3]))

    def findIslandInZone(self, s1, s2):
        '''
            Find islands that s1 and s2 belong to and look for a
            connection between them, if they are in the zone.
        '''
        # return if s1 and s2 do not belong to the same zone
        if s1.zone != s2.zone and abs(s1.zone - s2.zone) > 1:
            f_str = f'Station{s1.id} and Station{s2.id} not in the same zone.'
            b_str = 'Please try other stations.'
            print(f_str, b_str)
            return -1
        if (s1.zone % 1 == 0 and s2.zone % 1 == 0
           and abs(s1.zone - s2.zone) >= 1):
            f_str = f'Station{s1.id} and Station{s2.id} not in the same zone.'
            b_str = 'Please try other stations.'
            print(f_str, b_str)
            return -1

        same_i = f'Station{s1.id} and Station{s2.id} are in the same island.'

        # Example: s1.zone = 1, s2.zone = 1.5
        if s1.zone % 1 == 0 and s2.zone % 1 != 0:
            island1 = self.__findAllIsland(s1)[0]
            if s2.zone - 0.5 == s1.zone:
                island2 = self.__findAllIsland(s2)[1]
            else:
                island2 = self.__findAllIsland(s2)[0]
            if s1 in island2 or s2 in island1:
                print(same_i)
                return -1
            str1 = f'Find connections between islands in zone{int(s1.zone)}.\n'
            str2 = f'Station{s1.id} is in island: {[s.id for s in island1]}\n'
            str3 = f'Station{s2.id} is in island: {[s.id for s in island2]}'
            print(str1 + str2 + str3)
            return self.findIslandConnection(island1, island2)

        # Example: s1.zone = 1.5, s2.zone = 1
        elif s1.zone % 1 != 0 and s2.zone % 1 == 0:
            if s1.zone - 0.5 == s2.zone:
                island1 = self.__findAllIsland(s1)[1]
            else:
                self.__findAllIsland(s1)[0]
            island2 = self.__findAllIsland(s2)[0]
            if s1 in island2 or s2 in island1:
                print(same_i)
                return -1
            str1 = f'Find connections between islands in zone{int(s2.zone)}.\n'
            str2 = f'Station{s1.id} is in island: {[s.id for s in island1]}\n'
            str3 = f'Station{s2.id} is in island: {[s.id for s in island2]}'
            print(str1 + str2 + str3)
            return self.findIslandConnection(island1, island2)

        # Example: s1.zone = 1, s2.zone = 1
        elif s1.zone % 1 == 0 and s2.zone % 1 == 0:
            island1 = self.__findAllIsland(s1)[0]
            island2 = self.__findAllIsland(s2)[0]
            if s1 in island2 or s2 in island1:
                print(same_i)
                return -1
            str1 = f'Find connections between islands in zone{int(s1.zone)}.\n'
            str2 = f'Station{s1.id} is in island: {[s.id for s in island1]}\n'
            str3 = f'Station{s2.id} is in island: {[s.id for s in island2]}'
            print(str1 + str2 + str3)
            return self.findIslandConnection(island1, island2)

        # if both stations' zones are float (1.5, 2.5, 3.5, et)
        else:
            # both stations are in the same zone
            if s1.zone == s2.zone:
                island1 = self.__findAllIsland(s1)[0]
                island2 = self.__findAllIsland(s2)[0]
                island3 = self.__findAllIsland(s1)[1]
                island4 = self.__findAllIsland(s2)[1]
                z_1 = int(s1.zone + 0.5)
                z_2 = int(s1.zone - 0.5)
                str1 = 'Find connections between islands'
                str2 = f' in zone{z_1} and zone{z_2}.'
                print(f'''{str1}{str2}
                Station{s1.id} is in island: {[s.id for s in island1]}
                Station{s2.id} is in island: {[s.id for s in island2]}
                Find connections between islands in {int(s1.zone-0.5)}.
                Station{s1.id} is in island: {[s.id for s in island3]}
                Station{s2.id} is in island: {[s.id for s in island4]}''')

                # Check two other islands if two of the
                # stations are in the same island
                if s1 in island2 or s2 in island1:
                    print(same_i)
                    self.findIslandConnection(island3, island4)
                elif s1 in island4 or s2 in island3:
                    print(same_i)
                    return self.findIslandConnection(island1, island2)
                else:
                    return self.findIslandConnection(island1,
                                                     island2,
                                                     island3,
                                                     island4)

            else:
                # island 1 and 2 station list
                i1_s_l = [s.id for s in island1]
                i2_s_l = [s.id for s in island2]
                str_2 = f'\nStation{s1.id} is in island: {i1_s_l}'
                str_3 = f'\nStation{s2.id} is in island: {i2_s_l}'
                # s1.zone > s2.zone
                if s1.zone - 1 == s2.zone:
                    island1 = self.__findAllIsland(s1)[1]
                    island2 = self.__findAllIsland(s2)[0]
                    if s1 in island2 or s2 in island1:
                        print(same_i)
                        return -1
                    zone = int(s1.zone-0.5)
                    str_1 = f'Find connections between islands in zone{zone}.'
                    print(str_1 + str_2 + str_3)
                # s1.zone < s2.zone
                else:
                    island1 = self.__findAllIsland(s1)[0]
                    island2 = self.__findAllIsland(s2)[1]
                    if s1 in island2 or s2 in island1:
                        print(same_i)
                        return -1
                    zone = int(s1.zone+0.5)
                    str_1 = f'Find connections between islands in zone{zone}.'
                    print(str_1 + str_2 + str_3)
                return self.findIslandConnection(island1, island2)
