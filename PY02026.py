n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Sắp xếp tập A và tập B theo thứ tự tăng dần
A = sorted(set(a))
B = sorted(set(b))

# Kiểm tra xem tập A và tập B có bằng nhau hay không
if len(A) != len(B):
    print("NO")
else:
    for i in range(len(A)):
        if A[i] != B[i]:
            print("NO")
            break
    else:
        print("YES")