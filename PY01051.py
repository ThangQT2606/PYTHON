t = int(input())
while( t > 0):
    t -= 1
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    sum = str(sum)
    if sum == sum[::-1] and int(sum)  > 10:
        print("YES")
    else:
        print("NO")
    