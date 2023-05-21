# Lấy dãy số từ input
numbers = []
for i in range(10):
    numbers.append(int(input()))

# Lọc các số có chia dư cho 42
unique_numbers = set()
for number in numbers:
    unique_numbers.add(number % 42)

# In ra số lượng số khác nhau tìm được
print(len(unique_numbers))