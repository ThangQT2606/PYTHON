s= str(input())
dem=0
dem1=0
for i in s:
    if i.isupper():
        dem+=1
    else:
        dem1+=1
if dem > dem1:
    print(s.upper())
else:
    print(s.lower())