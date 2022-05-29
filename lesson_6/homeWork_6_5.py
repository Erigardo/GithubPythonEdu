# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать
# переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение; создать экземпляры
# классов и проверить, что выведет описанный метод для каждого экземпляра.


# (канцелярская принадлежность)
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


# ручка
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Рисуем ручкой'


# карандаш
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        return f'Вы взяли {self.title}. Рисуем карандашом'


# маркер
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Рисуем маркером'


pen = Pen('Ручка')
print(pen.draw())
pencil = Pencil('Карандаш')
print(pencil.draw())
handle = Handle('Маркер')
print(handle.draw())
