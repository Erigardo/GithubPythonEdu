#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 6. Реализовать два небольших скрипта:
#
#     *итератор, генерирующий целые числа, начиная с указанного;
#     *итератор, повторяющий элементы некоторого списка, определённого заранее.
#
#     Подсказка: используйте функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Предусмотрите условие его завершения.
#     Например, в первом задании выводим целые числа, начиная с 3.
#     При достижении числа 10 — завершаем цикл.
#     Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

import sys
from itertools import cycle, count

# cycle_gen(str("ABED"))


if __name__ == "__main__":

    def gen_int(n):
        # итератор начинает счет с заданного числа
        iterator = count(start=n)
        for i in iterator:
            # К условию добавляем единицу тк индекс начинается с нуля
            if i == n + 10 + 1:
                print("Выполнено условие завершения цикла")
                break
            yield i
            # print(i)
            # return i


    def cycle_gen(x):
        iterator_c = cycle(x)
        r = 0
        for i in iterator_c:
            if r > 10:
                print("Выполнено условие завершения цикла")
                break
            yield i
            # print(i)
            # r += 1
            # return i


    n = 0
    if len(sys.argv) == 3:
        arg_name = ["Имя скрипта",
                    "Выполнение счетчика 'count'",
                    "Выполнение замкнутого цикла 'cycle'",
                    ]
        calc_args = [None]
        mistake = {}
        n = 0
        i = -1
        for param in sys.argv:
            i += 1
            calc_args.append(param)
            print(f"{arg_name[i]} --> {param}")
            if not param.isdigit():
                mistake[i] = param
        try:
            print(*calc_args)
            a = int(calc_args[2])
            b = str(calc_args[3])
            print("Параметр функции: ", a, type(a))
            print("Параметр функции: ", b, type(b))
            for i in (gen_int(a)):
                print(i)
            print("#", "-*-" * 15, "new script", "-*-" * 15)
            a = 0
            for j in (cycle_gen(b)):
                print(j)
                a += 1
                if a > len(b)-1:
                    print("Выполнено условие завершения цикла")
                    break

        except:
            del mistake[0]
            for key, value in mistake.items():
                print(f"Вы допустили ошибку параметре {key} со значением - {value} !")
    else:
        print("В командной строке введите имя фаила c 2-мя численными параметрами для cycle() и count()!")
