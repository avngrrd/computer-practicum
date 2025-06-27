import math

x = float(input("Input x: "))

if x <= 0:
    f = (1 + x) / math.sqrt(1 + x ** 2)
elif x < 1:
    f = -x + 2 * math.exp(-2 * x)
else:
    f = abs(2 - x) ** (1 / 3)

print(f"f({x}) = {f}") 