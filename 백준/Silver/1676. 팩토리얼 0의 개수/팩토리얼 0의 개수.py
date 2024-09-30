N = int(input())
Sum = 1
for i in range(N,0,-1):
    Sum *= i
lst = list(str(Sum))
cnt = 0
for i in range(len(lst)):
    if lst[-1] == '0':
        cnt += 1
        lst.pop()
    else:
        break
print(cnt)