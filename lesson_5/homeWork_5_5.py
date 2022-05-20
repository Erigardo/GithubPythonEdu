# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму
# чисел в файле и выводить её на экран.
from random import randint

my_file = open('filename.txt', 'w')
for i in range(10):
    a = str(randint(0, 99))
    my_file.write(" ".join(a))

numbers = my_file.readlines()
sum_num = 0
for i in numbers:
    stroke = i.split(' ')
    for k in stroke:
        sum_num += k

print(sum_num)
