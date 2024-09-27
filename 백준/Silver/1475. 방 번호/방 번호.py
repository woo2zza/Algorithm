num = list(map(int, input()))
bucket = [0] * 10

Max_buck = bucket[0]
ind_buk = 0
Max_69 = 0
for i in range(len(num)):
    bucket[num[i]] += 1
for i in range(len(bucket)):
    ind_buk = i

    if ind_buk == 6 or ind_buk == 9:
        Max_69 = round(bucket[6] + bucket[9] + 0.6) // 2
    else : 
        if bucket[i] > Max_buck:    
            Max_buck = bucket[i]
if Max_69 >= Max_buck:
    print(Max_69)
else: print(Max_buck)

