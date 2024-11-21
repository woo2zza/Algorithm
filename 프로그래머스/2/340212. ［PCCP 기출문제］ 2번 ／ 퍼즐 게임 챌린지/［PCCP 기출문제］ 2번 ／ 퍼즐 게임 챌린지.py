def solution(diffs, times, limit):
    low , high = 1, max(diffs)
    answer = high
    
    while low < high:
        level = int((low + high) / 2)
        time = times[0]
        
        for i in range(1, len(diffs)):
            k = 0
            if diffs[i] > level:
                k = diffs[i] - level
            time += (times[i] + times[i-1]) * k + times[i]
            
        if time <= limit:
            high = level
            answer = level
        else:
            low = level + 1
        

    return answer