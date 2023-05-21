s = input()
l = len(s)-1
dem = 0
k = ""
while True:
    dem += 1
    k = s[l] + k
    if l == 0:
        break
    if dem == 3:
        k = ',' + k
        dem = 0
    l -= 1
print(k)