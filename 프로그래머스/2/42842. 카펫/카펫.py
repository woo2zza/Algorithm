def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            shar = yellow // i
            if (shar * 2) + (i * 2) == brown - 4:
                return [shar+2 , i+2]

