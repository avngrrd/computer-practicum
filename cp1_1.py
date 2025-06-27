# Програма для обчислення значення Z за формулою

import math

c = float(input("Введіть значення c: "))

a = math.sqrt((c + 1) ** 3)
b = a ** 3 + 1
d = math.exp(b ** 2 + a ** 2)

Z = ((a * math.sqrt(b) + c * math.sqrt(d)) ** 3 * 2.1) / (a + b + c)

print(f"Результат: Z = {Z:.5f}")