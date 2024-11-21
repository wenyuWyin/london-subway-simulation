# Test for second week features
#   - Patrol Planning Problem and Islands
# Note coverage percentage for island.py can be low due to
# multiple helper functions that are not tested in this file.
# The correct final result indicates the correctness for helper functions.
try:
    from adjList import AdjList
    from dataLoader import DataLoader
    from TSPAlgo import TSP
    from island import Island
except ModuleNotFoundError:
    import sys
    path = sys.path[0]
    sys.path.append(path + '/subway/utils')
    sys.path.append(path + '/subway/shortestPath')
    sys.path.append(path + '/subway/structures')
    sys.path.append(path + '/subway/island')
    sys.path.append(path + '/subway/patrolPlanning')
    from adjList import AdjList
    from dataLoader import DataLoader
    from TSPAlgo import TSP
    from island import Island

# Initialize data needed for testing
file_path_1 = ['_dataset/london.stations - Test.csv',
               '_dataset/london.lines - Test.csv',
               '_dataset/london.connections - Test.csv']
data_loader_1 = DataLoader(file_path_1[0], file_path_1[1], file_path_1[2])
stations_1 = data_loader_1.loadStation()
lines_1 = data_loader_1.loadLine()
connections_1 = data_loader_1.loadConnections(stations_1, lines_1)
adjList_1 = AdjList(connections_1)

file_path_2 = ['_dataset/london.stations - Island.csv',
               '_dataset/london.lines - Island.csv',
               '_dataset/london.connections - Island.csv']
data_loader_2 = DataLoader(file_path_2[0], file_path_2[1], file_path_2[2])
stations_2 = data_loader_2.loadStation()
lines_2 = data_loader_2.loadLine()
connections_2 = data_loader_2.loadConnections(stations_2, lines_2)
adjList_2 = AdjList(connections_2)


def test_tsp():
    '''
        Test patrol planning problem
    '''
    start = stations_1[1]
    patrol_stations = stations_1

    tsp_algo = TSP(adjList_1, start, patrol_stations)
    tsp_algo.travellingSalesmanProblem()

    stations_tsp = []

    stations_tsp.append(start.id)
    for station in tsp_algo.shortest_path:
        stations_tsp.append(station.id)
    stations_tsp.append(start.id)

    # check if the order of stations are correct
    assert stations_tsp == [2, 5, 6, 4, 3, 7, 1, 8, 9, 2]


def test_island():
    '''
        Test island identifying problem
    '''
    island = Island(stations_2, connections_2, adjList_2)
    island.separateIslandInZone()

    zone_station_lists = []
    for _, stations in island.zone_graph.items():
        station_list = []
        for s in stations:
            station_list.append(s.id)
        zone_station_lists.append(station_list)

    # check if all islands are identified
    assert zone_station_lists == [[1, 4, 8], [2, 3, 4], [5, 6, 7, 9]]


def test_island_connection():
    '''
        Test finding a connection between islands
    '''
    island = Island(stations_2, connections_2, adjList_2)
    island.separateIslandInZone()
    final_path = island.findIslandInZone(stations_2[1], stations_2[3])

    intermediate_stations = set()
    for c in final_path.connections:
        intermediate_stations.add(c.s1.id)
        intermediate_stations.add(c.s2.id)

    # check if the path between islands is correct
    assert intermediate_stations == {3, 1, 4}
