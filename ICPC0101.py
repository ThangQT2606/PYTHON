n = int(input())
lst =[]
lst = list(map(int,input().split()))
while True:
    check = 0
    dem = 0
    k = len(lst) -1
    for i in range(len(lst)-1):
        if i + 1 < len(lst):
            if (lst[i] + lst[i+1] ) % 2 == 0:
                lst.pop(i)
                lst.pop(i)
            else:
                check += 1 
    if check == k:
        print(len(lst))
        break

