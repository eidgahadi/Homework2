n=int(input())
all_nums=list(map(int, input().strip().split(' ')))
negs, zeros, pos, totalnums=0,0,0,len(all_nums)

for i in range(n):
    if all_nums[i]<0:
        negs+=1
    elif all_nums[i]==0:
        zeros+=1
    else:
        pos+=1
print(round(pos/totalnums,3))
print(round(negs/totalnums,3))
print(round(zeros/totalnums,3))