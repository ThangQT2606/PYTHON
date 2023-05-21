def check(n):
    for i in range(0,len(n),2):
        if i % 2 == 0 and int(n[i]) == 0:
            return False
    return True


t = int(input())
while(t > 0):
    t -= 1
    n = input()
    tong = 0
    tich = 1
    
    k = n.replace('0','1')
    for i in range(0,len(k),2):
        tich = tich * int(k[i])
    print(tich,end=' ')
    for i in range(1,len(n),2):
        tong += int(n[i])
    print(tong)        
        # print()
            
        
        