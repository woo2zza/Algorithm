def find(x):
    if parent[x] != x:
        find(parent[x])
    return x

def union(x,y) :
    x = find(x)
    y = find(y)

    if x < y :
        parent[y] = x
    else :
        parent[x] = y

testcase = 0
while True:
    N = int(input())
    if N == 0:
        break
    
    parent = [i for i in range(N+1)]
    arr = {}
    testcase += 1
    for i in range(N):
        start, end = input().split()

        if not start in arr:
            arr[start] = len(arr) +1
        if not end in arr:
            arr[end] = len(arr) +1
        union(parent[arr[start]], parent[arr[end]])
    parent = set(parent)

    print(testcase, len(parent)-1)
