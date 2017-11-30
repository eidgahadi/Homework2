def key1(lst):
    return lst[0]
n = int(input())
lst = []
for i in range(n):
    inp = input().split()
    if i < n/2:
        pn = 0
    else:
        pn = 1
    lst.append([int(inp[0]), inp[1], pn])
ar = []
for i in range(100):
    ar.append([])
for l in lst:
    ar[l[0]].append(l)
for l in ar:
    for i in l:
        if i[2]:
            print(i[1], end = " ")
        else:
            print("-", end = " ")