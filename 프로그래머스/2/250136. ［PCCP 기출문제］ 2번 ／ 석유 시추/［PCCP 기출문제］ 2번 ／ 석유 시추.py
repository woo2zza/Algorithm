from collections import deque

def solution(land):
    height, width = len(land), len(land[0])
    answer = [0] * width
    visited = [[0] * width for _ in range(height)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def bfs(start_x, start_y):
        cnt = 1  
        visited[start_x][start_y] = 1
        q = deque()
        q.append((start_x, start_y))
        min_col, max_col = start_y, start_y  

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    cnt += 1
                    q.append((nx, ny))
                    min_col = min(min_col, ny)
                    max_col = max(max_col, ny)

        for col in range(min_col, max_col + 1):
            answer[col] += cnt

    for i in range(height):
        for j in range(width):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    return max(answer)
