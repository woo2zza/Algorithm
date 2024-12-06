def solution(strArr):
    answer = []
    idx = 1
    for word in strArr:
        if idx % 2 == 0:
            answer.append(word.upper())
            idx += 1
        else:
            answer.append(word.lower())
            idx += 1
    
    return answer