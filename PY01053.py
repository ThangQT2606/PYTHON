t = int(input())
while(t > 0):
    t -= 1
    s = str(input())
    tong =0
    for i in range(len(s)):
        tong = tong + int(s[i])
    if( tong % 3 == 0):
        print("YES")
    else:
        print("NO")
