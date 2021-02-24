#задаётся начальный граф
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

#инициализируем таблицу стоимостей
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = float('inf')

#задаётся таблица родителей
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

#проверенные узлы (узел не должен проверяться дважды)
visited = []

def check_nodes_positive(graph: dict):
    for elem in graph.keys():
        if isinstance(graph[elem], dict):
                if not check_nodes_positive(graph=graph[elem]):
                    return False
        else:
            for val in graph.values():
                if val < 0:
                    return False
    return True

def dijkstra(graph: dict):
    if not check_nodes_positive(graph):
        return

dijkstra(graph)