from collections import deque

def dfs(node, visited, net):
    queue = deque()
    queue.append(node)
    visited[node] = True
    
    while queue:
        node = queue.popleft()
        for i in net[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    
        

def solution(n, computers):
    
    l = len(computers[0])
    net = [set() for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(l):
            if computers[i][j] == 1:
                net[i + 1].add(j + 1)
                net[j + 1].add(i + 1)
    
    visited = [False] * (n + 1)
    
    ct = 0
    print(net)
    for i in range(1, n + 1):
        for j in net[i]:
            if not visited[j]:
                ct += 1
                dfs(j, visited, net)
    
    return ct
    
    
    