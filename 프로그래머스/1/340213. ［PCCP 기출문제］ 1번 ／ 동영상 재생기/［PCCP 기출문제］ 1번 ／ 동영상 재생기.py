
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
def minuteToSec(time):
    times = time.split(":")
    return int(times[0]) * 60 + int(times[1])

def totalSecToMin(time):
    minute = time//60
    second = time%60

    if minute >= 10:
        minute = str(minute)
    elif minute < 10:
        minute = "0" + str(minute)
    elif minute == 0:
        minute = "00"
    if second >= 10:
        second = str(second)
    elif second < 10:
        second = "0" + str(second)
    elif second == 0:
        second = "00"

    return minute + ":" + second

def solution(video_len, pos, op_start, op_end, commands):
    video_len = minuteToSec(video_len)
    pos = minuteToSec(pos)
    op_start = minuteToSec(op_start)
    op_end = minuteToSec(op_end)

    movement = {'next': 10, 'prev' : -10}
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        pos += movement[command]
        if video_len - pos < 10:
            pos = video_len
        if pos < 10:
            pos = 0
        if op_start <= pos <= op_end:
            pos = op_end

    answer = totalSecToMin(pos)
    return answer
