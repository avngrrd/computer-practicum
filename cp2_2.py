import math

x = float(input("Input x: "))

if -2 <= x <= 2:
    f = 2 * math.cos(2 * x)
else:
    f = abs(x)

print(f"f({x}) = {f}")