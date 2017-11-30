n = int(input())
arr = [int(i) for i in input().split()]
left = []
equal = [arr[0]]
right = []

for i in range(1, n):
    if arr[i] < arr[0]:
        left.append(arr[i])
    elif arr[i] == arr[0]:
        equal.append(arr[i])
    elif arr[i] > arr[0]:
        right.append(arr[i])
res = left + equal + right

print(' '.join([str(i) for i in res]))