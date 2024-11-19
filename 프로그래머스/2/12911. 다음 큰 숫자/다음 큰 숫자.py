def solution(n):
    result = list(bin(n)[2:])
    cnt = result.count('1')
    for i in range(n+1, n+100):
        if list(bin(i)[2:]).count('1') == cnt:
            return i
  