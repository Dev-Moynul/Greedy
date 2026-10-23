n = int(input())
t = n*(n+1) // 2
if t % 2 != 0:
    print("NO")
else:
    print("YES")
    tr = t // 2
    s1 = []
    s2 = []

    tr = t // 2
    for i in range(n, 0, -1):
        # print(i)
        if i <= tr:
            s1.append(i)
            tr -= i
        else:
            s2.append(i)
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)