n = int(input())
c = list(map(int, input().split()))
c.sort(reverse = True)
t = sum(c)
r = cnt = 0
for i in c:
    r += i
    cnt += 1
    if r > t - r:
        break
print(cnt)