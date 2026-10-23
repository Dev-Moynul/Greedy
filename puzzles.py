n, m = map(int, input().split())
f = list(map(int, input().split()))
 
f.sort()
d = []
 
for i in range(m - n + 1):
    d.append(f[i + n - 1] - f[i])
print(min(d))