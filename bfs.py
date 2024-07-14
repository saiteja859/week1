#Implementing BFS(Breadth-First Search)
from queue import Queue

def bfs(graph, start_node):
    visited = set()
    queue = Queue()

    queue.put(start_node)
    visited.add(start_node)

    while not queue.empty():
        current_node = queue.get()
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)


if __name__ == "__main__":

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("BFS starting from node 'A':")
    bfs(graph, 'A')
