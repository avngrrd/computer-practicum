z = float(input("Введіть дійсне число z: "))
m = int(input("Введіть натуральне число m: "))

S = 0
for k in range(1, m + 1):
    S += -z ** k / k

print("Результат обчислення суми S:", S)
