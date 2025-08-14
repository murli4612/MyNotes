def dfs_iterative(graph, start):
    stack = [start]

    while stack:
        node = stack.pop()
        print(node)
        for neighbour in graph[node]:
            stack.append(neighbour)
# def dfs_recursive(graph, node):
#     print(node)
#     for neighbour in graph[node]:
#         dfs_recursive(graph, neighbour)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

dfs_iterative(graph, 'A')
# A C  E B D F
# dfs_recursive(graph ,"A") 
# A B D F CE
