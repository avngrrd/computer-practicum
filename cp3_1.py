def count_unique_chars(word):
    return len(set(word))

word = input("Введіть слово: ")
print("Кількість різних символів у слові:", count_unique_chars(word))