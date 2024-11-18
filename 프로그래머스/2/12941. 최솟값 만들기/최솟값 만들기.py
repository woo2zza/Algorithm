def solution(A,B):
    answer = 0
    lst_A = []
    lst_B = []
    for i in A:
        lst_A.append(int(i))
    lst_A.sort()
    for i in B:
        lst_B.append(int(i))
    lst_A.sort()
    lst_B.sort(reverse = True)
    for i in range(len(A)):
        result = lst_A[i] * lst_B[i]
        answer += result
    return answer