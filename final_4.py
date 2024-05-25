import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional attribute to store node color
        self.id = str(uuid.uuid4())  # Unique identifier for each node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Use id and store node value
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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Use node value for labels

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap(arr):
    heap = []
    for item in arr:
        heap.append(item)
        current_idx = len(heap) - 1
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2
            if heap[current_idx] < heap[parent_idx]:
                heap[current_idx], heap[parent_idx] = heap[parent_idx], heap[current_idx]
                current_idx = parent_idx
            else:
                break
    return heap

def draw_heap(heap):
    heap_tree = nx.DiGraph()
    pos = {}
    node_ids = []

    for i, val in enumerate(heap):
        node_id = str(uuid.uuid4())
        node_ids.append(node_id)

        # Calculate position based on level and horizontal offset
        level = i.bit_length()  # Determine the level of the node
        offset = i - (2**(level - 1) - 1)  # Determine the offset within the level
        x = offset * 2 - (2**(level - 1) - 1)
        y = -level
        pos[node_id] = (x, y)

        heap_tree.add_node(node_id, label=val)
        if i > 0:
            parent_id = node_ids[(i - 1) // 2]
            heap_tree.add_edge(parent_id, node_id)
    
    labels = {node: heap_tree.nodes[node]['label'] for node in heap_tree.nodes()}
    plt.figure(figsize=(12, 8))
    nx.draw(heap_tree, pos, labels=labels, arrows=False, node_size=2500, node_color="skyblue")
    plt.show()

# Create a binary tree and visualize it
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

draw_tree(root)

# Create a heap from an array and visualize it
array = [4, 10, 3, 5, 1, 7, 9]
heap = build_heap(array)
draw_heap(heap)
