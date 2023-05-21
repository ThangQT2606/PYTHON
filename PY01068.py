n, k = map(int, input().split())
a = set(list(map(str, input().split())))
b = list(a)
b.sort()
# print(b)
x = ['']*k
def Try(i, pos):
    for j in range(pos, len(b)):
        x[i] = b[j]
        if i == k-1:
            for it in x:
                print(it, end = ' ')
            print()
        else:
            Try(i+1, j + 1)
Try(0, 0)
