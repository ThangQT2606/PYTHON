from math import*

if __name__ == '__main__':
    t = int(input())
    cnt = 0
    while cnt < t:
        cnt += 1
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        ok = True
        check = n//2
        d = dict()
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for val, fre in d.items():
            if fre > check:
                ok = False
                print(val)
                break
        if ok:
            print('NO')
            