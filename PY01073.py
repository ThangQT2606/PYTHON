s = input()
n = len(s)
used = [0] * n
a = ['']*n

def Try(i):
    if i == n:
        for x in a:
            print(x, end='')
        print()
        return
    for j in range(n):
        if used[j] == 0:
            a[i] = s[j]
            used[j] = 1
            Try(i + 1)
            used[j] = 0
Try(0)