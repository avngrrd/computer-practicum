import math

def exp_neg_taylor(x, eps=1e-5):
    term = 1
    sum_ = term
    k = 1
    iterations = 1
    while abs(term) > eps:
        term *= -x / k
        sum_ += term
        k += 1
        iterations += 1
    return 1 + sum_, iterations

a = float(input("Введіть a (початок інтервалу): "))   # 0.5
b = float(input("Введіть b (кінець інтервалу): "))    # 1
m = int(input("Введіть кількість обчислювань (не менше 10): "))
if m < 10:
    m = 10

eps = 1e-5
h = (b - a) / (m - 1)
x = a

print(f"{'x':>10} {'~f(x)':>15} {'f(x)':>15} {'Точність':>15} {'Ітерацій':>12}")
print("-" * 70)

i = 0
while i < m:
    approx, iters = exp_neg_taylor(x, eps)
    exact = 1 + math.exp(-x)
    error = abs(approx - exact)
    print(f"{x:10.5f} {approx:15.8f} {exact:15.8f} {error:15.8f} {iters:12}")
    x += h
    i += 1
