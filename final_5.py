import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Unique identifier for each node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    node_colors = [colors.get(node, "#000000") for node in tree.nodes()]

    plt.figure(figsize=(12, 8))
    plt.title(title)  # Adding the title to the plot
    nx.draw(tree, pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def generate_colors(n):
    """Generate n lighter colors"""
    base_color = mcolors.hex2color("#1296F0")
    white = mcolors.hex2color("#FFFFFF")
    colors = [mcolors.to_hex([(1 - (i / n)) * base_color[j] + (i / n) * white[j] for j in range(3)]) for i in range(n)]
    return colors

def dfs_traversal(node, visited, order):
    if node:
        visited.append(node.id)
        order.append(node.id)
        dfs_traversal(node.left, visited, order)
        dfs_traversal(node.right, visited, order)

def bfs_traversal(node):
    visited = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        visited.append(current.id)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return visited

# Creating the tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Performing DFS traversal
dfs_visited = []
dfs_order = []
dfs_traversal(root, dfs_visited, dfs_order)

# Performing BFS traversal
bfs_visited = bfs_traversal(root)

# Generating colors for DFS
dfs_colors = generate_colors(len(dfs_visited))
dfs_color_map = {node_id: color for node_id, color in zip(dfs_visited, dfs_colors)}

# Generating colors for BFS
bfs_colors = generate_colors(len(bfs_visited))
bfs_color_map = {node_id: color for node_id, color in zip(bfs_visited, bfs_colors)}

# Visualizing DFS traversal
print("DFS Traversal Order:", dfs_order)
draw_tree(root, dfs_color_map, "DFS Traversal")  # Adding title for DFS traversal

# Visualizing BFS traversal
print("BFS Traversal Order:", bfs_visited)
draw_tree(root, bfs_color_map, "BFS Traversal")  # Adding title for BFS traversal
