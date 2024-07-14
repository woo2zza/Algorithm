arr = [['A','B','C'], ['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

result = 2
lst = []
S = list(input())
for i in arr:
    result += 1
    for j in S:
        if j in i:
            lst.append(result)

print(sum(lst))
