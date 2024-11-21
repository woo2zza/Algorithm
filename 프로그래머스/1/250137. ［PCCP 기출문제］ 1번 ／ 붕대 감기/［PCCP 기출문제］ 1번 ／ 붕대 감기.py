def solution(bandage, health, attacks):
    answer = health
    Max_heel, Sec_heel, Plus_heel = bandage
    
    now_time = 0
    idx = 0
    stack = 0
    
    while 1:
        now_time += 1  
        
        if answer <= 0:
            return -1
    
        if idx == len(attacks):
            break
        
        if now_time == attacks[idx][0]:
            answer -= attacks[idx][1]
            idx += 1
            stack = 0
            
        else:
            stack += 1
            answer = min(health, answer + Sec_heel)
            
            if stack == Max_heel:
                answer = min(health, Plus_heel + answer)
                stack = 0
    
    return answer

