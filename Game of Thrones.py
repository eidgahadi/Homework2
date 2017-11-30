string = input()

l = []
m = []
for c in string:
    n = 0
    if c in m:
        continue
    for i in range(0, len(string)):
        if string[i] == c:
            n = n + 1
    m.append(c)
    l.append(n)

k = 0
for j in l:
    if j % 2 == 1:
        k = k + 1

if k > 1:
    print("NO")
else:
    print("YES")