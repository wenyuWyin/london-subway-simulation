# Test first week features
#   - Dataloader, metricsComputer, Dijkstra, A*
try:
    from dataLoader import DataLoader
    from metricsHandler import MetricsHandler
    from adjList import AdjList
    from pathGenerator import PathGenerator
    from dijkstra import Dijkstra
    from AStar import Astar
except ModuleNotFoundError:
    import sys
    path = sys.path[0]
    sys.path.append(path + '/subway/utils')
    sys.path.append(path + '/subway/shortestPath')
    sys.path.append(path + '/subway/structures')
    from dataLoader import DataLoader
    from metricsHandler import MetricsHandler
    from adjList import AdjList
    from pathGenerator import PathGenerator
    from dijkstra import Dijkstra
    from AStar import Astar


'''Two test graphs: London Subway as case 1 and Self-defined graph as case 2'''

file_paths_1 = ['_dataset/london.stations.csv',
                '_dataset/london.lines.csv',
                '_dataset/london.connections.csv']
file_paths_2 = ['_dataset/london.stations - Test.csv',
                '_dataset/london.lines - Test.csv',
                '_dataset/london.connections - Test.csv']

data_loader_1 = DataLoader(file_paths_1[0], file_paths_1[1], file_paths_1[2])
data_loader_2 = DataLoader(file_paths_2[0], file_paths_2[1], file_paths_2[2])

stations_1 = data_loader_1.loadStation()
lines_1 = data_loader_1.loadLine()
connections_1 = data_loader_1.loadConnections(stations_1, lines_1)
adjList_1 = AdjList(connections_1)

stations_2 = data_loader_2.loadStation()
lines_2 = data_loader_2.loadLine()
connections_2 = data_loader_2.loadConnections(stations_2, lines_2)
adjList_2 = AdjList(connections_2)


def test_loadData():
    '''Using self-defined test cases'''

    data_loader = DataLoader(file_paths_2[0], file_paths_2[1], file_paths_2[2])

    stations = data_loader.loadStation()
    lines = data_loader.loadLine()
    connections = data_loader.loadConnections(stations, lines)
    assert [station.lat for station in stations] == [51.5028, 51.5143,
                                                     51.5154, 51.5107,
                                                     51.5407, 51.5322,
                                                     51.5653, 51.6164,
                                                     51.4905]
    assert [line.name for line in lines] == ["Bakerloo Line",
                                             "Circle Line",
                                             "Hammersmith & City Line",
                                             "Jubilee Line",
                                             "Victoria Line"]
    assert [connection.time for connection in connections] == [3, 2, 3, 1,
                                                               1, 3, 1, 3,
                                                               2, 4, 1, 2,
                                                               1, 4, 3, 2,
                                                               3, 6, 4, 3]


def test_metrics():
    '''Using self-defined test cases'''
    metrics_handler = MetricsHandler(stations_2, lines_2, connections_2)

    num_nodes = metrics_handler.computeNodeNum()
    num_edges = metrics_handler.computeEdgeNum()
    avg_deg = round(metrics_handler.computeAvgDeg(), 2)
    assert num_nodes == 9
    assert num_edges == 20
    assert avg_deg == 4.44


def test_dijkstra_2():
    '''
        Test for Dijkstra using a self-defined graph
    '''
    start = stations_2[3]
    end = stations_2[7]

    dijkstra_algo = Dijkstra(adjList_2, stations_2, connections_2, start, end)
    path_gen = PathGenerator()
    edgeTo, _ = dijkstra_algo.findShortestPath()
    _ = path_gen.generatePath(edgeTo, start, end, connections_2)

    stations_in_path = set()
    for c in path_gen.pickTopInitinerary().connections:
        stations_in_path.add(c.s1.id)
        stations_in_path.add(c.s2.id)

    # check if the path includes correct stations
    assert stations_in_path == {4, 3, 1, 8}


def test_astar_2():
    '''
        Test for A* using a self-defined graph
    '''
    start = stations_2[3]
    end = stations_2[7]

    astar_algo = Astar(adjList_2, stations_2, connections_2, start, end)

    paths = astar_algo.runAlgorithm()

    stations_in_path = set()

    for c in paths[0].connections:
        stations_in_path.add(c.s1.id)
        stations_in_path.add(c.s2.id)

    # check if the path includes correct stations
    assert stations_in_path == {1, 3, 4, 8}


def test_dijkstra_1():
    '''
        Test for Dijkstra using the given graph
    '''
    start = stations_1[171]
    end = stations_1[219]

    dijkstra_algo = Dijkstra(adjList_1, stations_1, connections_1, start, end)
    path_gen = PathGenerator()
    edgeTo, _ = dijkstra_algo.findShortestPath()
    _ = path_gen.generatePath(edgeTo, start, end, connections_1)

    stations_in_path = set()
    for c in path_gen.pickTopInitinerary().connections:
        stations_in_path.add(c.s1.id)
        stations_in_path.add(c.s2.id)

    # check if the path includes correct stations
    assert stations_in_path == {197, 151, 60, 126, 48, 250}


def test_astar_1():
    '''
        Test for A* using the given graph
    '''
    start = stations_1[171]
    end = stations_1[219]

    astar_algo = Astar(adjList_1, stations_1, connections_1, start, end)

    paths = astar_algo.runAlgorithm()

    stations_in_path = set()
    for c in paths[0].connections:
        stations_in_path.add(c.s1.id)
        stations_in_path.add(c.s2.id)

    # check if the path includes correct stations
    assert stations_in_path == {197, 151, 60, 126, 48, 250}
