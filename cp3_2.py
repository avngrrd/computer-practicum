def generate_numbers(limit):
    numbers = set()

    for n in range(int(limit**0.5) + 1):
        for m in range(int(limit**0.5) + 1):
            value = n**2 + m**2
            if 1 <= value <= limit:
                numbers.add(value)

    return sorted(numbers)

limit = int(input("Введіть верхню межу діапазону: "))
result = generate_numbers(limit)

print("Множина чисел у порядку зростання:")
print(result)