t = int(input())
while( t > 0):
    t -= 1
    n = input()
    dem=1
    for i in range(len(n)-1):
        if(n[i] == n[i+1]):
            dem+=1
        else:
            print(dem ,str(n[i]),sep='',end='') 
            dem =1  
    print(dem,str(n[len(n)-1]),sep='',end='')
    print()