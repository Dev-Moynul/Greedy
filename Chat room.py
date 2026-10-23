s = input().strip()
tr = "hello"
i = 0

for ch in s:
    if i < len(tr) and ch == tr[i]:
        i += 1
if i == len(tr):
    print("YES")
else:
    print("NO")