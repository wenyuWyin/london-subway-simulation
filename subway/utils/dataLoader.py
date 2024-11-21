import csv
import sys
from station import Station
from line import Line
from connection import Connection


class DataLoader():
    '''
        DataLoader class loads the data from .csv files
    '''

    def __init__(self, station_path, line_path, connection_path):
        '''
            Initialize a class instance
        '''
        self.station_path = sys.path[0] + "/" + station_path
        self.line_path = sys.path[0] + "/" + line_path
        self.connection_path = sys.path[0] + "/" + connection_path

    def loadStation(self):
        '''
            Load information about stations from .csv file to a list
        '''
        stations = []
        # open .csv file
        with open(self.station_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            next(spamreader, None)
            # parse the opened file
            for row in spamreader:
                row_elements = [s.strip("") for s in row]
                id = int(row_elements[0])
                lat = float(row_elements[1])
                lon = float(row_elements[2])
                name = row_elements[3]
                d_name = row_elements[4]
                zone = float(row_elements[5])
                total_lines = int(row_elements[6])
                rail = int(row_elements[7])
                stations.append(Station(id, lat, lon, name,
                                d_name, zone, total_lines, rail))
        return stations

    def loadLine(self):
        '''
            Load information about lines from .csv file to a list
        '''
        lines = []
        # open .csv file
        with open(self.line_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            next(spamreader, None)
            # parse the opened file
            for row in spamreader:
                row_elements = [s.strip("") for s in row]
                line = int(row_elements[0])
                name = row_elements[1]
                color = row_elements[2]
                stripe = row_elements[3]
                lines.append(Line(line, name, color, stripe))
        return lines

    def loadConnections(self, stations, lines):
        '''
            Load information about lines from .csv file to a list
        '''
        connections = []
        # open the .csv file
        with open(self.connection_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            next(spamreader, None)
            for row in spamreader:          # parse the opened file
                row_elements = [s.strip("") for s in row]
                station1 = next((station for station in stations
                                if station.id == int(row_elements[0])), None)
                station2 = next((station for station in stations
                                if station.id == int(row_elements[1])), None)
                line = next((line for line in lines
                            if line.id == int(row_elements[2])), None)
                time = int(row_elements[3])
                connections.append(Connection(station1, station2, line, time))
        return connections
