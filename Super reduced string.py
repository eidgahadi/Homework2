s = input().strip()

i = 0
while(True):
    if(i >= len(s)-1):
        break
    if(s[i]==s[i+1]):
        s = s[:i] + s[i+2:]
        i=0
        continue
    i+=1
if(len(s)==0):
    print('Empty String')
else:
    print(s)
    