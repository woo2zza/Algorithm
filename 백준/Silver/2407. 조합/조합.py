import sys

n,m = map(int, input().split())

Total_de = 1
Total_mo = 1
cnt = 0

for i in range(m, 0, -1):
    cnt += 1
    Total_de *= i

for i in range(n, n-cnt, -1):
    Total_mo *= i

print(Total_mo // Total_de)