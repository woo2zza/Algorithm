def solution(n):
    pre = 0
    now = 1
    for i in range(2, n+1):
        now, pre = pre + now, now
    return now % 1234567
