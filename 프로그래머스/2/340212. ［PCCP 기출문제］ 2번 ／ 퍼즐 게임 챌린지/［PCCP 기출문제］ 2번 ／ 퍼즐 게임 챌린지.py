def solution(diffs, times, limit):
    max_level = max(diffs) 
    l = 1
    answer = max_level 

    while l < max_level:
        level = int((l + max_level) / 2) 
        time = times[0]  
        
        for i in range(1, len(diffs)):
            k = 0
            if level < diffs[i]:
                k = diffs[i] - level
            time += (times[i] + times[i -1]) * k + times[i]

        if time <= limit:
            max_level = level
            answer = level  
        else:
            l = level +1    

    return answer


    