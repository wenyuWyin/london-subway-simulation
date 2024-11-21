import numpy
import random
from randomGen import RandomGenerator
from connection import Connection


class RandomNormal(RandomGenerator):
    '''
        RandomNormal class inherits from RandomGenerator
        and generates connections that are normally distributed
    '''

    def __init__(self, station_num, degree):
        '''
            Initialize a class instance
        '''
        super().__init__(station_num, degree)
        self.all_degrees = self.getNormalDegree()
        self.all_degrees.sort()
        self.assignStationDegree()
        self.getEnhancedConnection()

    def getEnhancedConnection(self):
        '''
            Generate normally distributed connections
        '''
        exist_connections = {s: 0 for s in self.s_list}
        all_possible_connections = {s1: [s2 for s2 in self.s_list if s2 != s1]
                                    for s1 in self.s_list}
        connections = []
        # Generate proper number of connections based on pre-assigned value
        for s1 in self.s_list:
            try_count = 0
            # Add more connections until the maximum degree of s1 is reached
            while exist_connections[s1] < self.degree_of_station[s1]:
                s2 = random.choice(all_possible_connections[s1])
                try_count += 1
                if exist_connections[s2] < self.degree_of_station[s2]:
                    # Randomly choose a station to connect with
                    # all_possible_connections[s1].remove(s2)
                    # all_possible_connections[s2].remove(s1)
                    exist_connections[s1] += 1
                    exist_connections[s2] += 1
                    connections.append(Connection(s1, s2,
                                       random.choice(self.l_list),
                                       random.randint(1, 4)))
                # Stop looking for connections for the current node after
                # a certain threshold
                if try_count >= self.s_num * (0.80):
                    break
        self.c_list = connections

    def getNormalDegree(self):
        '''
            Return a numpy array of numbers that are normally
            distributed by a mean of self.degree and standard deviation of 1
        '''
        return numpy.random.normal(self.degree, 1, self.s_num)

    def __getStationDegree(self):
        '''
            Generate a list that specifies the number of stations
            of each degree (1 < degree < degree * 2 - 1).
        '''
        degree_list = [0] * (self.degree * 2 - 1)
        start_degree = 1.5
        # Iterate through the degree list and increment
        # the number of stations at corresponding index
        for degree in self.all_degrees:
            if degree < start_degree or degree > self.degree * 2 - 1:
                degree_list[int((start_degree-1.5)/1)] += 1
            else:
                start_degree += 1
                degree_list[int((start_degree-1.5)/1)] += 1
        return degree_list

    def assignStationDegree(self):
        '''
            Assign each station with a degree number
        '''
        station_of_degree_dict = {i: [] for i in range(1, self.degree * 2)}
        stations = self.s_list.copy()
        num_station_degree = self.__getStationDegree()

        # Example: If there is 5 stations with degree 1,
        # then add 5 random stations to the list at station_of_degree_dict[5]
        for i, d in enumerate(num_station_degree):
            for _ in range(d):
                new_s = random.choice(stations)
                stations.remove(new_s)
                # i + 1 ensures the station has at least one connection
                station_of_degree_dict[i+1].append(new_s)

        # Convert station_of_degree_dict to a dictionary
        # that describes how many degrees each station has
        self.degree_of_station = {s: 0 for s in stations}
        for degree, stations in station_of_degree_dict.items():
            for s in stations:
                self.degree_of_station[s] = degree
