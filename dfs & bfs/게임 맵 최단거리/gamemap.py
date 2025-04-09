from collections import deque

def bfs(x, y, maps):
    m = len(maps)
    n = len(maps[0])
    queue = deque()
    queue.append((x, y))
    
    move_x = [1, -1, 0, 0]
    move_y = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + move_x[i], y + move_y[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                    
def solution(maps):
    #가로, 세로 고정으로 주어짐
    m = len(maps)
    n = len(maps[0])
    
    bfs(0, 0, maps)
    
    print(maps)
    ans = maps[-1][-1]
    # 문제 보니 m>1, n>1 조건 있으므로 굳이 필요 X
    if ans > 1 or m == 1 and n == 1:
        return ans
    else:
        return -1
        