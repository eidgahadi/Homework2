s = int(input())
ar = list(map(int, input().split()))
v = ar[-1]
for j in range(s-1, 0, -1):
        if v >= ar[j-1]:
                ar[j] = v
                break
        ar[j] = ar[j-1]
        print(' '.join(map(str, ar)))
else:
        ar[0] = v
print(' '.join(map(str, ar)))