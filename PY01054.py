t = int(input())
while ( t > 0):
    t -= 1
    n = input()
    n = n.replace("0","")
    tich = 1
    for i in n:
        tich = tich * int(i)
    print(tich)