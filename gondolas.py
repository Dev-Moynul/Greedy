n, lm = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
l, r = 0, n-1
g = 0
while l <= r:
    if w[l] + w[r] <= lm:
        l += 1
    r -= 1
    g += 1
print(g)