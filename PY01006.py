t = int(input())
while(t > 0):
    t -=1
    s = str(input())
    dem=0   
    dem1=0
    for i in range(len(s)):
        if s[i] == '4' or s[i] == '7':
            dem += 1
    if dem == len(s):
        print("YES")
    else:
        print("NO")