def solution(video_len, pos, op_start, op_end, commands):
    now_time = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    video_time = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
    start_open = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    end_open = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])
    
    for Input in commands:
                
        if start_open <= now_time and now_time <= end_open:
            now_time = end_open
        
        if Input == 'next':
            now_time += 10
            if  now_time >= video_time:
                now_time = video_time
            
        elif Input == 'prev':
            now_time -= 10
            if now_time <= 0:
                now_time = 0
        
        if start_open <= now_time and now_time <= end_open:
            now_time = end_open
    
    result = str(now_time // 60)
    return f'{result.zfill(2)}:{str(now_time%60).zfill(2)}'
