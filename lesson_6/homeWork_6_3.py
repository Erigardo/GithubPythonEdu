# 3. Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход); последний атрибут должен быть защищённым
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}; создать
# класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии (get_total_income); проверить работу примера на реальных
# данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы
# экземпляров.


class Worker:
    # атрибуты: name, surname, position (должность), income (доход)
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        # ссылаться на словарь, содержащий элементы: оклад и премия
        self._income = {"wage": wage, "bonus": bonus}


# класс Position (должность) на базе класса Worker
class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


# создать экземпляры класса Position
man = Position("Alexander", "Gavrilov", "manager", 2800, 350)
print(man.get_full_name())
print(man.position)
print(man.get_total_income())
man2 = Position("Olga", "Sorokina", "consultant", 40000, 2500)
print(man2.get_full_name())
print(man2.position)
print(man2.get_total_income())
man3 = Position("James", "Cook", "servant", 15000, 13700)
print(man3.get_full_name())
print(man3.position)
print(man3.get_total_income())

# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
