from collections import deque
def BFS(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)       
graph = {
    'A': ['B','C'],
    'B': ['A','D','C'],
    'C': ['A','F','G'],
    'D': ['B'],
    'E': ['B','H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}                
BFS(graph,'E') 
