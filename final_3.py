import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):    
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    previous = [-1] * n
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        # Якщо відстань до u більша за вже знайдену, пропустити
        if current_dist > dist[u]:
            continue
        
        # Перевірити всіх сусідів вершини u
        for v, weight in graph[u]:
            distance = current_dist + weight
            
            # Якщо знайдено коротший шлях до вершини v
            if distance < dist[v]:
                dist[v] = distance
                previous[v] = u
                heapq.heappush(priority_queue, (distance, v))
    
    return dist, previous

# Приклад використання
# Граф подано у вигляді списку суміжності: граф[i] містить список (сусід, вага)
graph = [
    [(1, 4), (2, 1)],    # Сусіди вершини 0
    [(3, 1)],            # Сусіди вершини 1
    [(1, 2), (3, 5)],    # Сусіди вершини 2
    [(4, 3)],            # Сусіди вершини 3
    []                   # Сусіди вершини 4
]

start_vertex = 0
dist, previous = dijkstra(graph, start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}: {dist}")
print(f"Попередні вершини: {previous}")

# Відновлення шляху до конкретної вершини (наприклад, до вершини 4)
def get_path(previous, target):
    path = []
    while target != -1:
        path.append(target)
        target = previous[target]
    path.reverse()
    return path

target_vertex = 4
path = get_path(previous, target_vertex)
print(f"Найкоротший шлях до вершини {target_vertex}: {path}")

# Візуалізація графа
def draw_graph(graph, dist, previous, start_vertex):
    G = nx.DiGraph()
    
    # Додавання ребер до графа
    for u in range(len(graph)):
        for v, weight in graph[u]:
            G.add_edge(u, v, weight=weight)
    
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f'{weight}' for u, v, weight in G.edges(data='weight')}
    
    # Малювання графа
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Підсвічування найкоротших шляхів
    for target_vertex in range(len(graph)):
        if target_vertex != start_vertex:
            path = get_path(previous, target_vertex)
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    
    plt.title(f"Граф і найкоротші шляхи від вершини {start_vertex}")
    plt.show()

draw_graph(graph, dist, previous, start_vertex)
