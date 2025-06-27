n = int(input("введіть число від 1 до 9: "))

if 1 <= n <= 9:
    i = 0
    while i < n:
        j = n
        while j > i:
            print(j, end=' ')
            j -= 1
        print()
        i += 1
else:
    print("число повинно бути від 1 до 9.")
