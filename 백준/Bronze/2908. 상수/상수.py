arr = list(input().split(' '))
result = []
for newArr in arr:
    new = int(''.join(reversed(newArr)))
    result.append(new)
print(max(result))
