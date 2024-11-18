def solution(s):
    result = []
    answer = s.split(' ')
    
    for char in answer:
        if char != '':
            result.append(char[0].upper() + char[1:].lower())
        else:
            result.append(char)
        
    return " ".join(result)
