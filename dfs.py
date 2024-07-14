#Implementing DFS(Depth-First-search)
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)

        for neighbor in reversed(graph[current_node]):
            if neighbor not in visited:
                stack.append(neighbor)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("DFS starting from node 'A':")
    dfs(graph, 'A')

