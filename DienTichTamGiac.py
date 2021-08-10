# Bài này sẽ tính diện tích qua công thức herong:
# cv = a + b + c
# p = cv/2
# dt = sqrt(p * (p - a) * (p - b) * (p - c))

from math import *
print("CHƯƠNG TRÌNH TÍNH DIỆN TÍCH TAM GIÁC:")
a = float(input("Nhập cạnh a > 0: "))
b = float(input("Nhập cạnh b > 0: "))
c = float(input("Nhập cạnh c > 0: "))

if (a <= 0 or c <= 0 or b <= 0) or(a + b) <= c or (a + c) <= b or (b + c) <= a:
    print("Tam giác không hợp lệ")
else:
    cv = a + b + c
    p = cv / 2 # Nửa chu vi
    dt = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Diện tích:", dt)
