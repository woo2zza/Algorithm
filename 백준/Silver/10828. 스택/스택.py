import sys
num = int(sys.stdin.readline())

lst = []
for i in range(num):
    st = sys.stdin.readline().split()
    if st[0] == 'top' :
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    elif st[0] == 'size':
        print(len(lst))
    elif st[0] == 'empty':
        if not lst:
            print(1)
        elif len(lst) > 0:
            print(0)
    elif st[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            A = lst.pop()
            print(A)
    else:
        lst.append(st[1])
