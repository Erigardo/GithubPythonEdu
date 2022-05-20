# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


f = open("filename7.txt")
f_w = open("filename7.txt", "a+")
strokes = f.readlines()
profit_company_list = []
company_profit_dict_list = []
for stroke in strokes:
    # print(str(stroke))
    str_n = str(stroke)  # (int(stroke[2]) - int(stroke[3]))
    # Получаем список
    split_str = (str_n.split(" "))
    # Убираем "\n"
    r_split_str = [line.rstrip() for line in split_str]
    # компании
    company = r_split_str[0]
    profit = int(r_split_str[2]) - int(r_split_str[3])
    # профитные компании
    company_profit = [company, profit]
    company_profit_dict = {company: profit}
    company_profit_dict_list.append(company_profit_dict)
    if profit > 0:
        profit_company_list.append(company_profit)
        print(f"Доход {company} составляет {profit}$")
    else:
        print(f"Убыток {company} составляет {profit}$")

# print(profit_company_list)
d = 0
for i in profit_company_list:
    d += i[1]

# средний доход по компаниям
medium_d = d / len(profit_company_list)
print(f"Средний доход по безубыточным организациям: {medium_d}")
print(company_profit_dict_list)

import json

dictionary = company_profit_dict_list
# добавим отступов
jsonString = json.dumps(dictionary, indent=4)
# print(dictionary)
# print(jsonString)
# Здесь мы используем оператор with, чтобы открыть файл
with f_w as outfile:
    # используем метод json.dump, чтобы записать наши словари в файл
    json.dump(jsonString, outfile)


# Coca-cola ООО 200000 75000
# H&M ОАО 40000 15000
# Unilever Corp 100000 35000
# Samsung ООО 95000 125000
# Hyundai ОАО 100000 21000
