from collections import deque

''' Depth First Search (DFS) '''
def dfs(x):
    # print(x, end=' ')
    visited[x] = True
    for y in graph[x]:
        if not(visited[y]):
            dfs(y)
            
''' Breadth First Search (BFS) '''
def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        x = q.popleft()
        # print(x, end=' ')
        for y in graph[x]:
            if not visited[y]:
                q.append(y)
                visited[y] = True

n = int(input())
m = int(input())
start = 1

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
dfs(start)
print(visited.count(True) - 1)

'''
BFS
visited = [False] * (n + 1)
bfs(start)
print(visited.count(True) - 1)
'''

'''
Input Data
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
