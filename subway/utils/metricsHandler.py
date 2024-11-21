import matplotlib.pyplot as plt


class MetricsHandler():
    '''
        MetricsHandler class computes various metrics of the
        subway system and plots the metrics
    '''

    def __init__(self, station_list, line_list, connection_list):
        '''
            Initialize a class instance
        '''
        self.station_list = station_list
        self.line_list = line_list
        self.connection_list = connection_list

    def computeNodeNum(self):
        '''
            Compute the number of stations in the subway system
        '''
        return len(self.station_list)

    def computeEdgeNum(self):
        '''
            Compute the total number of connections in the subway system
        '''
        return len(self.connection_list)

    def computeNodeDeg(self, node):
        '''
            Compute the degree given a station
            (helper function for computeAvgDeg())
        '''
        count = 0

        for edge in self.connection_list:
            if node.id == edge.s1.id or node.id == edge.s2.id:
                count += 1

        return count

    def computeAvgDeg(self):
        '''
            Compute the average degree of all stations
        '''
        deg_sum = sum([self.computeNodeDeg(n) for n in self.station_list])
        return deg_sum / self.computeNodeNum()

    def plot(self):
        '''
            Plot the metrics using matplotlib
            x-axis: possible degrees
            y-axis: number of stations with the degree
        '''
        num_stations = self.computeNodeNum()

        deg_dic = {}
        for i in range(num_stations):
            deg_of_node = self.computeNodeDeg(self.station_list[i])
            if self.computeNodeDeg(self.station_list[i]) not in deg_dic.keys():
                deg_dic[deg_of_node] = 1
            else:
                deg_dic[deg_of_node] += 1

        plt.bar(deg_dic.keys(), deg_dic.values())
        plt.title("Distribution of Node's Degree")
        plt.xlabel('Degree')
        plt.ylabel('Number of Stations')
        plt.show()
