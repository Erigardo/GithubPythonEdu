# Реализовать программу работы с органическими клетками,
# состоящими из ячеек. Необходимо создать класс Клетка.
class Cell:

    # В его конструкторе инициализировать параметр, соответствующий
    # количеству ячеек клетки (целое число).
    def __init__(self, fragments):
        self.fragments = fragments

    def table_cells(self, rows):  # ord(U+1F648)
        return '\n'.join(['🦠' * rows for _ in range(self.fragments // rows)]) + '\n' + '😎' * (self.fragments % rows)

    def __str__(self):
        return f'{self.fragments}'

    def __add__(self, other):
        print('Сумма клеток составляет: ')
        return self.fragments + other.fragments

    def __sub__(self, other):
        print(f"Вычитание клеток ({self.fragments}) и ({other})")
        return (self.fragments - other.fragments) \
            if self.fragments - other.fragments > 0 \
            else "Первая клетка меньше второй!"

    def __mul__(self, other):
        print('Умножение клеток: ')
        return self.fragments * other.fragments

    def __floordiv__(self, other):
        print("Деление клеток: ")
        return self.fragments // other.fragments


first_cell = Cell(15)
second_cell = Cell(5)
print(second_cell.__add__(first_cell))
print(first_cell.__sub__(second_cell))
print(first_cell * second_cell)
print(first_cell // second_cell)
print(first_cell.table_cells(6))
print(second_cell.table_cells(5))

# print(first_cell//)

#     def __init__(self, parts_of_cell=5, cells=1):
#         self.cell = [["*"] * parts_of_cell]
#         print(f"Фрагменты клетки {self.cell}")
#         self.cells = cells
#         self.cells = self.cell*self.cells
#         if len(self.cells) > 1:
#             print(f"Клетки {self.cells}")
#         else:
#             print(f"Клетка {self.cells}")
#
#     # В классе должны быть реализованы методы перегрузки арифметических операторов:
#     def __add__(self, new_cell=None):
#         # self.parts_of_cell += new_cell
#         if new_cell is None:
#             new_cell = ['*', '*', '*', '*', '*']
#         else:
#             new_cell = ["*"] * new_cell
#             if len(new_cell) > 5:
#                 cell_full = len(new_cell) // 5
#                 cell_not_full = len(new_cell) % 5
#                 new_cell = self.cell*cell_full + ['*']*cell_not_full
#         return self.cells + new_cell
#
#     def __sub__(self, new_cell=None):
#         if new_cell is None:
#             new_cell = ['*', '*', '*', '*', '*']
#         else:
#             new_cell = ["*"] * new_cell
#             if len(new_cell) > 1:
#                 cell_full = len(new_cell) // 5
#                 cell_not_full = len(new_cell) % 5
#                 new_cell = self.cell * cell_full + ['*'] * cell_not_full
#         return self.cells + new_cell
#
#     # сложение (__add__()), вычитание (__sub__()),
#     # умножение (__mul__()), деление (__truediv__()).
#
#     def __mul__(self):
#         pass
#
#     def __truediv__(self, other):
#         # В методе деления должно осуществляться округление значения до целого числа.
#         len(self.cell) / other
#
#
# c = Cell(5, 2)
# print(c.__add__(15))

# Данные методы должны применяться только к клеткам и
# выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) деление клеток, соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек
# общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять
# только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей
# клетки определяется как произведение количества ячеек этих
# двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей
# клетки определяется как целочисленное деление количества ячеек
# этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество
# ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество
# ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.

#
# class Cell:
#     def __init__(self, quantity):
#         self.quantity = int(quantity)
#         # self.result = result
#
#     def __str__(self):
#         return f'Результат операции {self.quantity * "*"}'
#
#     def __add__(self, other):
#         # self.result = Cell(self.quantity + other.quantity)
#         return Cell(self.quantity + other.quantity)
#
#     def __sub__(self, other):
#         '''
#         Выдает ошибку о том, что результат не число  при вычислении
#         if int(Cell(self.quantity - other.quantity)) > 0:
#             return Cell(int(self.quantity - other.quantity))
#         else:
#             return f'Операция вычитания невозможна'""
#         '''
#         return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')
#
#         # return Cell(int(self.quantity - other.quantity))
#
#     def __mul__(self, other):
#         # self.result = Cell(int(self.quantity * other.quantity))
#         return Cell(int(self.quantity * other.quantity))
#
#     def __truediv__(self, other):
#         # self.result = Cell(round(self.quantity // other.quantity))
#         return Cell(round(self.quantity // other.quantity))
#
#     def make_order(self, cells_in_row):
#         row = ''
#         for i in range(int(self.quantity / cells_in_row)):
#             row += f'{"*" * cells_in_row} \\n'
#         row += f'{"*" * (self.quantity % cells_in_row)}'
#         return row
#
#
# cells1 = Cell(33)
# cells2 = Cell(9)
# print(cells1)
# print(cells1 + cells2)
# print(cells2 - cells1)
# print(cells2.make_order(5))
# print(cells1.make_order(10))
# print(cells1 / cells2)
