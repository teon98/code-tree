arr = list(map(int, input().split()))

find = 0
for i in range(len(arr)):
    if arr[i] == 0:
        find = i
        break

if find-4 < 0 :
    print(sum(arr[find-1::-1]))
else:
    print(sum(arr[find-1:find-4:-1]))