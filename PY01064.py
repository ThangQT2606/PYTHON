def xau(n):
    s = "A"
    for i in range(2, n+1):
        s = s + chr(i+64) + s
    return s

t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    s = xau(n)
    # print(s)
    if k <= len(s) // 2 + 1:
        print(s[k-1])
    else:
        s = s[::-1]
        print(s[len(s)-k])
