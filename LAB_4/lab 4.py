# Bài 1: Nhập n, tìm số Finacci thứ n bằng while
n = int(input("Nhập n: "))
if n == 0:
    print(f"Số Fibonacci thứ {n} là: 0")
elif n == 1:
    print(f"Số Fibonacci thứ {n} là: 1")
else:
    a = 0
    b = 1
    i = 2

    while i <= n:
        c = a + b
        a = b
        b = c
        i += 1
    print(f"Số Fibonacci thứ {n} là: {b}")

# Bài 2: Viết chương trình cho phép nhập mật khẩu liên tục cho đến khi đúng "123456"
mk = input("Nhập mật khẩu: ")
while mk != "123456":
    mk = input("Sai mật khẩu, yêu cầu nhập lại: ")

print("Đăng nhập thành công")

# Bài 3: Nhập số n. Tìm ước số lớn nhất của n (khác n)
n = int(input("Nhập n: "))
max = 1
for i in range(1, n):
    if n % i == 0:
        max = i
print(f"Ước số lớn nhất của {n} là: {max}")

# Bài 4: Nhập số liên tục cho đến khi nhập số 0 thì dừng.
# Tính tổng các số
# Đếm số lượng số
# Tìm số lớn nhất
so = int(input("Nhập số bất kỳ: "))

tong = 0
dem = 0

if so == 0:
    print("Không có số nào được nhập")
else:
    lon_nhat = so

    while so != 0:
        tong += so
        dem += 1
        
        if so > lon_nhat:
            lon_nhat = so
        
        so = int(input("Nhập số bất kỳ: "))

    print("--------------------")
    print("Tổng các số là:", tong)
    print("Số lượng số là:", dem)
    print("Số lớn nhất là:", lon_nhat)

# Bài 5: Nhập số n. Kiểm tra n có phải số đối xứng (palindrome) không.
#Ví dụ: 121 → đúng, 123 → sai
n = int(input("Nhập n: "))
temp = n
dao = 0

while temp > 0:
    chu_so = temp % 10
    dao = dao * 10 + chu_so
    temp //= 10

if dao == n:
    print(n, "là số đối xứng")
else:
    print(n, "không là số đối xứng")

# Bài 6: Nhập n. Kiểm tra n có phải số Armstrong không
# VD: 153 = 1³ + 5³ + 3³
n = int(input("Nhập n: "))
temp = n
k = len(str(n))
tong = 0

while temp > 0:
    so_cuoi = temp % 10
    tong += so_cuoi**k
    temp //= 10

if tong == n:
    print(n, "là số Armstrong")
else:
    print(n, "không là số Armstrong")

# Bài 7: In bảng cửu chương từ 2 → 9 bằng while lồng nhau
i = 2
while i <= 9:
    print(f"\nBảng {i}: ")

    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j}")
        j += 1

    i += 1

# Bài 8: Viết chương trình:
# Nhập số n
# Tách từng chữ số
# Tính:
# Tổng chữ số
# Tích chữ số
# Số đảo
n = int(input("Nhập n: "))
tong = 0
tich = 1
dao = 0

while n > 0:
    chu_so = n % 10
    tong += chu_so
    tich *= chu_so
    dao = dao * 10 + chu_so
    n //= 10

print("Tổng các chữ số là:", tong)
print("Tích các chữ số là:", tich)
print("Số đảo là:", dao)

# Bài 9: Viết chương trình menu:
# 1. Cộng
# 2. Trừ
# 3. Nhân
# 4. Chia
# 0. Thoát
while True:
    print("\n===== MENU =====")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")

    chon = int(input("Chọn: "))
    if chon == 0:
        print("Thoát chương trình")
        break

    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))

    if chon == 1:
        print("Kết quả:", a+b)
    elif chon == 1:
        print("Kết quả:", a-b)
    elif chon == 3:
        print("Kết quả:", a*b)
    elif chon == 4:
        print("Kết quả:", a/b)
    else:
        print("Chọn sai, yêu cầu nhập lại")

# Bài 10: In tam giác ngược:
# ****
# ***
# **
# *
i = 4
while i >= 1:

    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i -= 1

# Bài 11:
n = int(input("Nhập n: "))
while n <= 10:
    n = int(input("Nhập lại n (>10): "))

a = 1
S1 = 0
while a <= n:
    S1 += 6**a
    a += 1

a = 1
S2 = 0
while a <= n:
    S2 += 1/(3**(2*a-1))
    a += 1

a = 1
S3 = 0
while a <= n:
    S3 += ((-1)**a) * (a**2)
    a += 1

a = 1
S4 = 0
while a <= n:
    S4 += a * (a+1) * (a+2)
    a += 1

print("a) S1 =", S1)
print("b) S2 =", S2)
print("c) S3 =", S3)
print("d) S4 =", S4)