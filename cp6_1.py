import random

n = int(input("Enter the number of elements n: "))
a = [random.randint(0, 50) for _ in range(n)]
print("Po4aktoviy list:", a)

for i in range(n - 1):
    max_index = max(range(n - i), key=a.__getitem__)
    a[max_index], a[n - 1 - i] = a[n - 1 - i], a[max_index]

print("Vidsortovaniy list in descending order:", a)
