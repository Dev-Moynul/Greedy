n = int(input())
arr = list(map(int, input().split()))
m = 0
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        m += arr[i-1] - arr[i]
        arr[i] = arr[i - 1]
print(m)