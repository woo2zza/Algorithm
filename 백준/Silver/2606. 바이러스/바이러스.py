
from collections import deque

Com = int(input())
Net = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(Net)]

q = deque()
q.append(1)
used = [0] * (Com + 1)
used[1] = 1
while q:
    new = q.popleft()
    for i in range(Net):
        if arr[i][1] == new:
            if used[arr[i][0]] != 1: 
                used[arr[i][0]] = 1
                q.append(arr[i][0])
        if arr[i][0] == new:
            if used[arr[i][1]] != 1: 
                used[arr[i][1]] = 1
                q.append(arr[i][1])
print(sum(used)-1)

