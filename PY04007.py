class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __mul__(self, other):
        result = Matrix(self.rows, other.cols)

        for i in range(result.rows):
            for j in range(result.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum

        return result

t = int(input())
while t > 0:
    n, m = map(int, input().split())
    a = Matrix(n, m)
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            a.data[i][j] = row[j]
    a_transpose = Matrix(m, n)
    for i in range(n):
        for j in range(m):
            a_transpose.data[j][i] = a.data[i][j]
    result = a * a_transpose
    for i in range(result.rows):
        for j in range(result.cols):
            print(result.data[i][j], end=' ')
        print()
    t = t - 1
