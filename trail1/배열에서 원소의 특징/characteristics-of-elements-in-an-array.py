arr = list(map(int, input().split()))

x = 0
for i in range(len(arr)):
    if arr[i] % 3 == 0:
        x = i
        break

print(arr[x-1])