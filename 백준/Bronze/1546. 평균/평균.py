
N = int(input())
lst = list(map(int, input().split()))
maxValue = max(lst)
result = []
for i in lst:
    result.append(i / maxValue * 100)

print(sum(result) / N)