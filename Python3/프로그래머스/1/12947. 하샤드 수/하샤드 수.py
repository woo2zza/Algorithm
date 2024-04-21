def solution(x):
    answer = True
    num = list(map(int, str(x)))
    if x % int(sum(num)) == 0:
        answer = True
    else:
        answer = False

    return answer