class Connection():
    '''
        Connection class is used to represent all the
        connections between stations

        PS: the connections are undirected
    '''

    def __init__(self, station1, station2, line, time):
        '''
            Initialize a class instance
        '''
        self.s1 = station1
        self.s2 = station2
        self.line = line
        self.time = time

    def display_info(self):
        '''
            print all information about a connection
        '''
        str1 = f'station1_id: {self.s1.id} - station2_id: {self.s2.id}'
        str2 = f'line_id: {self.line.id} - time: {self.time}'
        print(f'{str1} - {str2}')
