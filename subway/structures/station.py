class Station():
    '''
        Station class is used to represent a staion in the subway system
    '''

    def __init__(self, id, lat, lon, name, display_name,
                 zone, total_lines, rail):
        '''
            Initialize a class instance
        '''
        self.id = id
        self.lat = lat
        self.lon = lon
        self.name = name
        self.zone = zone
        self.total_lines = total_lines
        self.rail = rail
        self.d_name = display_name if display_name != "NULL" else None

    def display_info(self):
        '''
            Print all information about a station
        '''
        print(f'id: {self.id} - name: {self.name} - rail: {self.rail}')
