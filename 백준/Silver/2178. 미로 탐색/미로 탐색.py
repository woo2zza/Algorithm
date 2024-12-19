from collections import deque

N, M = map(int, input().split())

arr = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

direct_x = [0, 0, -1, 1]
direct_y = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y, 1)) 
    visited[x][y] = 1

    while q:
        nx, ny, cnt = q.popleft()
        
        if nx == N - 1 and ny == M - 1:
            return cnt
        
        for i in range(4):
            dx = nx + direct_x[i]
            dy = ny + direct_y[i]
            
            if 0 <= dx < N and 0 <= dy < M and visited[dx][dy] == 0 and arr[dx][dy] == '1':
                visited[dx][dy] = 1
                q.append((dx, dy, cnt + 1))
    
    return -1  

result = bfs(0, 0)
print(result)
