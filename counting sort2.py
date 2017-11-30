n=int(input().strip())
arr=[int(i) for i in input().strip().split(' ')]
for i in range(100):
    if i in arr:
        print((str(i)+' ')*arr.count(i),end='')