def solution(n):
    answer = n + 1
    zero = bin(n)[2:].count('1')
    while(zero != bin(answer)[2:].count('1')):
        answer += 1
    return answer