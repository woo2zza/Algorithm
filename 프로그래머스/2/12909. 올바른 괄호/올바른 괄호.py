def solution(s):
    stack =[]

    for i in range(0,len(s)):    
        if  s[i] == '(' :
            stack.append(s[i])
        elif stack :
            stack.pop()
        else :       
            return False

    return not stack 