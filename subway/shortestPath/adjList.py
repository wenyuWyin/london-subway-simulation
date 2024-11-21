class AdjList():
    '''
        Adjlist class converts all connections to an adjacency list and
        performs operations to obtain informations about the list
    '''

    def __init__(self, connection_list):
        '''
            Initialize a class instance
        '''
        self.setAdjList(connection_list)

    def setAdjList(self, connection_list):
        '''
            Convert all connections to an adjacency list
        '''
        self.adj_list = {}
        for connection in connection_list:
            s1 = connection.s1
            s2 = connection.s2
            line = connection.line
            time = connection.time
            if s1 in self.adj_list:
                if s2 in self.adj_list[s1]:
                    self.adj_list[s1][s2].append((line, time))
                else:
                    self.adj_list[s1][s2] = [(line, time)]
            else:
                self.adj_list[s1] = {}
                self.adj_list[s1][s2] = [(line, time)]

            # make the adjacency list symmetric
            # (representing an undirected graph)
            if s2 in self.adj_list:
                if s1 in self.adj_list[s2]:
                    self.adj_list[s2][s1].append((line, time))
                else:
                    self.adj_list[s2][s1] = [(line, time)]
            else:
                self.adj_list[s2] = {}
                self.adj_list[s2][s1] = [(line, time)]

    def getOutEdges(self, station):
        '''
            Obtain all lines come out of station
            Sample output: [(station1, line2, 3),
                            (station2, line4, 1), (station5, line1, 2)]
        '''
        out_edges = []
        for key, value in self.adj_list[station].items():
            for line, _ in value:
                # out_edges.append((key, line_info[0], line_info[1]))
                out_edges.append((key, line))
        return out_edges

    def getTime(self, station1, station2, line):
        '''
            Get the time that is needed to travel from station1
            to station2 via a certain line
        '''
        for current_line in self.adj_list[station1][station2]:
            if current_line[0] == line:
                return current_line[1]

    def getAllTime(self, station1, station2):
        '''
            Get the time that is needed to travel from station1
            to station2 without given the line
        '''
        return self.adj_list[station1][station2][0][1]
