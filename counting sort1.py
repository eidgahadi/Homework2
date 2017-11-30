V = int(input())
k = list(map(int, input().split()))
list = []
for i in range(100):
    list.append(k.count(i))
print(*list)
