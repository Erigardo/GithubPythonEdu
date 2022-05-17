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
import itertools

if __name__ == "__main__":
    n = 0
    if len(sys.argv) == 2:
        arg_name = ["Имя скрипта",
                    "Генерация с указанного числа"
                    ]
        calc_d = [None]
        mistake = {}
        n = 0
        i = -1
        for param in sys.argv:
            i += 1
            calc_d.append(param)
            print(f"{arg_name[i]} --> {param}")
            if not param.isdigit():
                mistake[i] = param
        try:
            argum = int(arg_name[1])
            my_list = itertools.count(argum)
            print(my_list)
        except:
            del mistake[0]
            for key, value in mistake.items():
                print(f"Вы допустили ошибку параметре {key} со значением - {value} !")
    else:
        print("В командной строке введите имя фаила c одним целочисленным параметром.")
