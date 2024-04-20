def solution(n):
    answer = 0
    lst = sorted(list(map(str, str(n))), reverse = True)
    answer = int("".join(lst))
    
 
    return answer