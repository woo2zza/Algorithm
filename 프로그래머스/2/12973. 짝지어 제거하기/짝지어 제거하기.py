def solution(s):
    stack = []
    lst = list(s)
    stack.append(lst[0])
    
    for i in range(1, len(lst)):
        if len(stack) == 0:
            stack.append(lst[i])
        elif stack[-1] == lst[i]:
            stack.pop()
        else:
            stack.append(lst[i])
    
    if len(stack) == 0: 
        return 1
    else:
        return 0
