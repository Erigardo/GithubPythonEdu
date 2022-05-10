# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


my_list = []
while True:
    symbol = input("Введите значения элементов:... или введите Quit:  ")
    if symbol == "Quit":
        for i in range(0, len(my_list) - 1, 2):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        break
    try:
        my_list.append(symbol)
        elements = len(my_list)
    except:
        break

print(my_list)
