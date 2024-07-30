result = []
resultNum = 0
resultCol = 0
resultRow = 0
for i in range(9):
    arr = list(map(int, input().split(' ')))
    maxNum = max(arr)
    maxNumIndex = arr.index(maxNum) 
    result.append([maxNum,i, maxNumIndex])

for i in range(9):
    if resultNum < result[i][0]:
        resultNum = result[i][0]
        resultCol = result[i][2]
        resultRow = result[i][1]
print(resultNum)
print(f'{resultRow+1} {resultCol+1}')