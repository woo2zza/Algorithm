def solution(numbers):
    cnt = 0
    for i in numbers:
        cnt += 1
    answer = sum(numbers) / cnt
    return answer