import math

k = math.pi / 20
m = math.pi / 10
n = math.pi / 1

x = m
while x <= n:
    y = math.cos(x) + math.sqrt(x)
    print(f"x = {x:.4f}, y = {y:.4f}")
    x += k
