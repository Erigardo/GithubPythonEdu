# Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для
# вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации
# операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять
# поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

from itertools import zip_longest


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str("\n".join(["\t".join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])


m = [[1, 2, 3], [4, 5, 6], [7, 8]]
n = [[1, 2, 3], [4, 5, 6]]

matrix_1 = Matrix(m)
matrix_2 = Matrix(n)
print(matrix_1)
print(matrix_1+matrix_2)
