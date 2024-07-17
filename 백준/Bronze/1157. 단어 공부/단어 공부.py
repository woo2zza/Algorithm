bucket = [0] * 26
arr = list(input().upper())
for i in arr:
    bucket[ord(i)-65] += 1

if bucket.count(max(bucket)) >= 2:
        print('?')
else:
    print(chr(bucket.index(max(bucket))+65))
