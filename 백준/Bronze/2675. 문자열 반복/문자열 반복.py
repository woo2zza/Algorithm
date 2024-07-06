t = int(input())
for i in range(t):
    a, b = input().split()
    for q in b:
        print(int(a)*q, end = '')
    print()