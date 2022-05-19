# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


my_file = open("filename.txt", "r")
my_file_w = open("filename.txt", "a+")
stroke = my_file.readlines()
russian_list = ["Один", "Два", "Три", "Четыре"]
new_list = []
print(stroke)
c = 0
stroke_r = ''
for i in stroke:
    # делим строку на слова
    words = i.split(' ')
    stroke = words
    # меняем элементы в начале строки
    stroke[0] = russian_list[c]
    # Конвертируем список в строку
    stroke_r = (" ".join(map(str, stroke)))
    my_file_w.write(stroke_r)
    c += 1