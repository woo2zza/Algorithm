arr = list(input())
Flag = 1
for i in range(len(arr)//2):
    if arr[i] != arr[len(arr) -i-1]:
        Flag = 0
        break
print(Flag)