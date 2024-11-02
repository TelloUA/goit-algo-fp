import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited: # поки купа не пуста, але мені треба оновлювати відстані кожен раз
        # знаходження вершини з найменшою відстанню серед невідвіданих
        min_heap = [(distances[vertex], vertex) for vertex in unvisited if vertex in distances]
        heapq.heapify(min_heap) # побудова купи
        current_vertex = min_heap[0][1] # можна не виймати, бо нам не потрібна перебудова цієї купи

        # якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        # передивляємося сусідні до графа вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

graph = {
    'A': {'B': 7, 'C': 9, 'F': 14},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9, 'G': 7},
    'F': {'A': 14, 'C': 2, 'E': 9},
    'G': {'E': 7, 'H': 5, 'I': 11},
    'H': {'G': 5, 'I': 6, 'J': 4},
    'I': {'G': 11, 'H': 6, 'J': 10, 'K': 7},
    'J': {'H': 4, 'I': 10, 'K': 6, 'L': 12},
    'K': {'I': 7, 'J': 6, 'L': 8},
    'L': {'J': 12, 'K': 8}
}

# Виклик функції для вершини A
print(dijkstra(graph, 'A'))
