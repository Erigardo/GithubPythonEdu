#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
# заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

import sys

if __name__ == "__main__":
    n = 0
    if len(sys.argv) == 4:
        arg_name = ["Имя скрипта",
                    "Выработка в часах",
                    "Ставка в час",
                    "Премия сотрудника"
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
            zp = int(calc_d[2]) * int(calc_d[3]) + int(calc_d[4])
            print(f"Заработная плата сотрудника составляет: {zp}")
        except:
            del mistake[0]
            for key, value in mistake.items():
                print(f"Вы допустили ошибку параметре {key} со значением - {value} !")
    else:
        print("В командной строке введите имя фаила c 3-мя численными параметрами.")
