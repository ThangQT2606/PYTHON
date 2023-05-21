def count_coin_pairs(grid):
    n = len(grid)
    row_count = dict()  # Từ điển đếm số đồng xu trên từng hàng
    col_count = dict()  # Từ điển đếm số đồng xu trên từng cột
    pair_count = 0      # Biến đếm số cặp đồng xu

    # Đếm số đồng xu trên từng hàng và từng cột
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'C':
                row_count[i] = row_count.get(i, 0) + 1
                col_count[j] = col_count.get(j, 0) + 1

    # Đếm số cặp đồng xu trong cùng một hàng
    for count in row_count.values():
        if count > 1:
            pair_count += count * (count - 1) // 2

    # Đếm số cặp đồng xu trong cùng một cột
    for count in col_count.values():
        if count > 1:
            pair_count += count * (count - 1) // 2

    return pair_count

n = int(input())
a = []
for i in range(n):
    b = list(map(str, input()))
    a.append(b)
print(count_coin_pairs(a))
