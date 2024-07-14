#creating a graph and accessing adjacent nodes of  a given node
graph = {}
adj_list = []
n = int(input("Enter the number of nodes in the graph :"))
for i in range (n):
    node = input(f"Enter node {i+1}: ")
    adj = int(input("Enter number of adjacent nodes :"))
    for j in range (adj):
        adj_node = input(f"enter adjacent node {j+1}: " )
        adj_list.append(adj_node)
    graph[node] = adj_list
    adj_list = []
node2 = input("Enter the node to display it's adjacent nodes :")
print(f"Adjacent nodes of {node2} are: ",graph[node2])
