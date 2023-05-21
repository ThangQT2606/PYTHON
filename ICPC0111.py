t = int(input())
while(t >0):
    t -= 1
    n,d=map(int,input().split())
    lst = []
    lst = list(map(int,input().split()))
    b = lst[d:]+lst[:d]
    for i in b:
        print(i , end=" ")
    print()
    