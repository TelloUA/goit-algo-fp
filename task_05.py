import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
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

# (залишив з попередньої задачі)
def create_tree(heap):
    nodes = [Node(value) for value in heap]  # робимо обʼєкти Node
    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(heap):
            nodes[i].left = nodes[left_index]  # логіка лівого нащадка
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]  # логіка правого нащадка
    return nodes[0]  # корінь дерева

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# робота зі зміною кольоруб вибрав зелений
def generate_color(step, total_steps):
    # починаємо з темного, закінчуємо світлим
    green_intensity = int(180 * (step / total_steps) + 75)  # 255 - світлий, 0 - темний
    return f'#{0:02X}{green_intensity:02X}{0:02X}'  # тільки змінюємо зелений

def dfs_iterative(root, size):
    if root is None:
        return

    visited = set()
    stack = [root]  # використовуємо стек для зберігання вузлів

    while stack:
        node = stack.pop()  # вилучаємо вузол зі стеку
        if node not in visited:
            visited.add(node)  # відвідуємо вузол
            node.color = generate_color(len(visited), size) # проставляємо наступний колір
            
            # додаємо дочірні вузли до стеку
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def bfs_iterative(root, size):
    if root is None:
        return

    visited = set()
    queue = deque([root]) # використовуємо чергу для зберігання вузлів

    while queue: 
        node = queue.popleft() # беремо вузол зі стеку
        if node not in visited:
            visited.add(node) # відвідуємо вузол
            node.color = generate_color(len(visited), size) # проставляємо наступний колір

            # додаємо не відвідані вершини
            if node.left and node.left not in visited:
                queue.append(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)

# реалізація дерева
heap = [15, 3, 32, 21, 2, 5, 8, 22, 11, 12, 13, 24, 4]
heapq.heapify(heap)
root = create_tree(heap)

# проставлення кольору dfs обходу, та вивід дерева
dfs_iterative(root, len(heap)) 
draw_tree(root)

# проставлення кольору bfs обходу, та вивід дерева
bfs_iterative(root, len(heap))
draw_tree(root)
