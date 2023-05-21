from math import*

if __name__ == '__main__':
    t = int(input())
    cnt = 0
    while cnt < t:
        cnt += 1
        n = int(input())
        d = dict()
        a = []
        for i in range(n):
            x = int(input())
            a.append(x)
        a.sort()
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ln = -1e9
        for val, fre in d.items():
            if ln < fre:
                ln = fre
        for val, fre in d.items():
            if fre == ln:
                print(val)
                break