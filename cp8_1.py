import random

def generate_random_time():
    return (random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

def input_time():
    h = int(input("Година (0-23): "))
    m = int(input("Хвилина (0-59): "))
    s = int(input("Секунда (0-59): "))
    return (h, m, s)

def show_all(times):
    for key, value in times.items():
        print(f"{key}: {value[0]:02d}:{value[1]:02d}:{value[2]:02d}")

def show_sorted(times):
    for key in sorted(times):
        t = times[key]
        print(f"{key}: {t[0]:02d}:{t[1]:02d}:{t[2]:02d}")

def compare_times(t1, t2):
    return (t1 > t2) - (t1 < t2)

def main():
    times = {i + 1: generate_random_time() for i in range(15)}

    while True:
        print("\nМеню:")
        print("1. Показати всі моменти часу")
        print("2. Додати момент часу")
        print("3. Видалити момент часу")
        print("4. Показати моменти часу за відсортованими ключами")
        print("5. Порівняти два моменти часу")
        print("6. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_all(times)
        elif choice == "2":
            key = int(input("Введіть ключ (число): "))
            if key in times:
                print("Такий ключ вже існує.")
            else:
                times[key] = input_time()
        elif choice == "3":
            key = int(input("Введіть ключ для видалення: "))
            if key in times:
                del times[key]
            else:
                print("Ключ не знайдено.")
        elif choice == "4":
            show_sorted(times)
        elif choice == "5":
            k1 = int(input("Перший ключ: "))
            k2 = int(input("Другий ключ: "))
            if k1 in times and k2 in times:
                t1 = times[k1]
                t2 = times[k2]
                result = compare_times(t1, t2)
                if result == 1:
                    print("Момент часу", k1, "пізніше.")
                elif result == -1:
                    print("Момент часу", k2, "пізніше.")
                else:
                    print("Обидва моменти однакові.")
            else:
                print("Один або обидва ключі не знайдено.")
        elif choice == "6":
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()
