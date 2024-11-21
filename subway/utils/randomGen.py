import random
import csv
from station import Station
from line import Line
from connection import Connection


class RandomGenerator():
    '''
        RandomGenerator class randomly generated
        a weighted undirected graph to simulate a subway system
    '''

    def __init__(self, station_num, degree):
        '''
            Initialize a class instance
        '''
        self.s_num = station_num
        self.l_num = int(station_num / 27.5)
        self.degree = degree

        self.genStationNames('_dataset/london.stations.csv')
        self.genLineNames('_dataset/london.lines.csv')

        self.genStation()
        self.genLine()
        self.genConnection()

    def genStation(self):
        '''
            Generate a list of stations with id range
            from 0 to self.s_num and random names
        '''
        stations = []
        for i in range(self.s_num):
            station_name = self.genStr()
            stations.append(Station(i, 50+random.random(),
                            -0.5+random.random(), station_name, station_name,
                            random.choice([i/2 for i in range(2, 11)]),
                                    None, None))
        self.s_list = stations

    def genLine(self):
        '''
            Generate a list of lines with id range
            from 0 to self.l_num and random names
        '''
        lines = []
        for i in range(self.l_num):
            lines.append(Line(i, self.genStr(0), None, None))
        self.l_list = lines

    def genConnection(self):
        '''
            Randomly generate connections between stations use random
            lines, weights, and times
        '''
        all_possible_connections = {s1: [s2 for s2 in self.s_list if s2 != s1]
                                    for s1 in self.s_list}
        connections = []
        for s1 in all_possible_connections.keys():
            # Create self.degree connections between s1
            # and other random stations
            for _ in range(self.degree):
                s2 = random.choice(all_possible_connections[s1])
                all_possible_connections[s1].remove(s2)
                all_possible_connections[s2].remove(s1)
                connections.append(Connection(s1, s2,
                                              random.choice(self.l_list),
                                              random.randint(1, 4)))
        self.c_list = connections

    def genStr(self, for_s=1):
        '''
            Return a random station name
            from station names that have already existed
            Input: for_s = 1 when generate name for stations
                   for_s = 0 when generate name for lines
        '''
        if for_s:
            new_name = random.choice(self.s_names)
            self.s_names.remove(new_name)
        else:
            new_name = random.choice(self.l_names)
            self.l_names.remove(new_name)
        return new_name

    def genStationNames(self, csv_path):
        '''
            Generate all possible station names
            given a csv path that stores station information
        '''
        station_names = []
        # open .csv file
        with open(csv_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            next(spamreader, None)
            # parse the opened file
            for row in spamreader:
                row_elements = [s.strip("") for s in row]
                name = row_elements[3]
                station_names.append(name)

        # Expanding the variety of names by adding integers to each name
        for i in range(int(self.s_num / len(station_names))):
            for s_name in station_names.copy():
                station_names.append(s_name + str(i+1))

        self.s_names = station_names

    def genLineNames(self, csv_path):
        '''
            Generate all possible line names given a csv path that
            stores line information
        '''
        line_names = []
        # open .csv file
        with open(csv_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            next(spamreader, None)
            # parse the opened file
            for row in spamreader:
                row_elements = [s.strip("") for s in row]
                name = row_elements[1]
                line_names.append(name)

        # Expanding the variety of names by adding integers to each name
        for i in range(int(self.l_num / len(line_names))):
            for l_name in line_names.copy():
                line_names.append(l_name + str(i+1))

        self.l_names = line_names
