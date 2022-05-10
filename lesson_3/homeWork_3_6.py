# 6. Реализовать функцию int_func(),
# принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# функция проверки на наличие латинских символов и букв
def latino(s):
    return s.isascii() and s.isalpha()


# функция фильтрации символов в слове
def filter_w(x):
    x = ''.join(ch for ch in x if ch.isascii() and ch.isalpha())
    return x


def int_func(*words):
    while True:
        sentence = words
        data_m = []
        data_r = []
        # для слова в предложении
        for word in sentence:
            # для буквы в слове
            if not latino(word):
                data_m.append(word)
            else:
                data_r.append(word)
        # способ вывода строки через .join
        return f"Вывод: {' '.join(data_r).lower()}"

# проверяем функцию
# int_func("Logan", "Solo", "Mega", "Lat", "Letter9")
