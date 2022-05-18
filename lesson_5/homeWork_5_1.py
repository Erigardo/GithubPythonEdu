#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

import sys

data = []
while True:
    print("Введите сообщение: ")
    answer = input()
    data.append(answer)
    original_stdout = sys.stdout  # Сохраним значение в оригинальный стандартный вывод
    with open('filename.txt', 'a+') as f:
        sys.stdout = f  # Сменим стандартный вывод на созданный нами фаил.
        print(answer)  # Запишем сообщение в фаил
        sys.stdout = original_stdout  # Конечно же, сбросим стандартный вывод к его оригинальному значению!
    if not answer:
        data.pop(-1)
        print("Запись в фаил завершена")
        print("Записи в фаил которые вы сделали: ")
        for i in data:
            print(i)
        break

# for input: Сорока ворока кашу варила деток кормила...
