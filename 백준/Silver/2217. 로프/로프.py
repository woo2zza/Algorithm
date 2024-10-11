arr = []

N = int(input())
for i in range(N):
    rope = int(input())
    arr.append(rope)

arr.sort()

result = []
for i in arr:
    result.append(i * N)
    N -= 1

print(max(result))