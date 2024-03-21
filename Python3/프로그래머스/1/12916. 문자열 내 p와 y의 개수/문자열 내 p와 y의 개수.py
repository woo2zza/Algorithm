def solution(s):
    answer = True
    countp = 0
    county = 0
    lst = [i.upper() for i in list(s)]
    for i in lst:
        if i == "P":
            countp += 1
        elif i == "Y":
            county += 1
    if countp == county:
        answer =True
    else:
        answer = False

    return answer