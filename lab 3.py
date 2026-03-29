# Bài 1:
# a) Viết chương trình để tính tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000
tong = 0
for i in range(2000, 4000+1):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 là:", tong)

# b) Viết chương trình để tính tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000
tong_b = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong_b += i
print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 là:", tong_b)

# Bài 2: In bảng cửu chương từ 1 đến 9 dạng bảng (2 chiều)
print("  ", end="")
for j in range(1, 10):
    print(f"{j:4}", end="")
print()

for i in range(1, 10):
    print(f"{i:2}", end="")

    for j in range(1, 10):
        print(f"{i*j:4}", end="")

    print()

# Bài 3: Viết chương trình nhập vào số hàng và thực hiện vẽ tam giác vuông rỗng.
# *
# **
# * *
# * *
# *****
n = int(input("Nhập số hàng: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Bài 4: 
import math
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Yêu cầu nhập lại"))
# a)
S1 = 0
for i in range(1, n+1):
    S1 += i
print("a) S1 =", S1)
# b)
S2 = 0
for i in range(1, n+1):
    S2 += 1/i
print("b) S2  =", S2)
# c)
S3 = 0
for i in range(1, n+1):
    S3 += 1/math.sqrt(2*i)
print("c) S3 =", S3)
# d)
S4 = 0
for i in range(1, n+1):
    if i % 2 == 0:
        S4 -= 1/i
    else:
        S4 += 1/i
print("d) S4 =", S4)

# Bài 5:
for i in range(1, 1001):
    if (i ** 0.5) == int(i ** 0.5):
        print(i, end=" ")

# Bài 6: Viết chương trình tính tổng nghịch đảo của số nguyên đầu tiên
n = int(input("Nhập n: "))
S1 = 0
for i in range(1, n+1):
    S1 += 1/i
print("S1 =", S1)

# Bài 7: Nhập n. Đếm số lượng số trong khoảng [1, n] có tổng chữ số là số chẵn
n = int(input("Nhập n: "))
dem = 0
for i in range(1, n+1):
    tong = 0
    temp = i

    while temp > 0:
        tong += temp % 10
        temp //= 10

    if tong % 2 == 0:
        dem += 1

print(f"Số lượng số chẵn trong khoảng [1, {n}] là: {dem}")

# Bài 8: Nhập n. Tìm số có tổng chữ số lớn nhất trong khoảng từ 1 đến n
n = int(input("Nhập n: "))
max_tong = 0
so_max = 0

for i in range(1, n+1):
    tong = 0
    temp = i

    while temp > 0:
        tong += temp % 10
        temp //= 10

    if tong > max_tong:
        max_tong = tong
        so_max = i

print(f"Số có tổng chữ số lớn nhất trong khoảng từ 1 đến {n} là: {so_max}")

# Bài 9: Nhập n. Tìm số có nhiều ước nhất trong khoảng từ 1 đến n
n = int(input("Nhập n: "))
max_uoc = 0
so_max = 0

for i in range(1, n+1):
    dem_uoc = 0

    for j in range(1, i+1):
        if i % j == 0:
            dem_uoc += 1

    if dem_uoc > max_uoc:
        max_uoc = dem_uoc
        so_max = i

print(f"Số có nhiều ước nhất trong khoảng 1 đến {n} là: {so_max}")
print(f"Số lượng các ước là: {max_uoc}")

# Bài 11: In ra n số Fibonacci đầu tiên bằng vòng lặp for
n = int(input("Nhập n: "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b 
    b = c

# Bài 12:
chu_cai_map = {
    'A':10, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18,
    'I':19, 'J':20, 'K':21, 'L':23, 'M':24, 'N':25, 'O':26, 'P':27,
    'Q':28, 'R':29, 'S':30, 'T':31, 'U':32, 'V':34, 'W':35, 'X':36,
    'Y':37, 'Z':38
}

container = input("Nhập mã container (10 ký tự): ").upper()

if len(container) != 10:
    print("Mã container phải đủ 10 ký tự!")
else:
    tong = 0

    for i in range(10):
        ky_tu = container[i]

        if i <= 3:  
            gia_tri = chu_cai_map[ky_tu]
        else:       
            gia_tri = int(ky_tu)

        trong_so = gia_tri * (2 ** i)

        tong += trong_so

    check_digit = tong % 11
    if check_digit == 10:
        check_digit = 0

    print(f"Số kiểm tra (check digit) của container {container} là: {check_digit}")