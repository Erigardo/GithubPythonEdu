# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда); опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} {self.speed}")

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась ")

    def turn(self, turn):  # (direction)
        if turn == "налево" or "направо":
            print(f"{self.name} повернула {turn}")
        else:
            print(f"{self.name} может поворачивать налево или направо!")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed} км/ч')
        if self.speed > 60:
            print(f'{self.name} превысила скорость')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=True)

    def police(self):
        if self.is_police is True:
            print(f'{self.name} машина полиции')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed} км/ч')
        if self.speed > 60:
            print(f'{self.name} превысила скорость')
        self.police()


# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

# print(Car.__dict__)

Jaguar = TownCar(speed=60, color="red", name="Jaguar")  # переопределите метод show_speed скорости свыше 60 (TownCar)
Jaguar.show_speed()
Aston_Martin = SportCar(speed=120, color="blue", name="Aston Martin")
Aston_Martin.show_speed()
Jeep = WorkCar(speed=70, color="green", name="Jeep")  # переопределите метод show_speed скорости свыше 40 (WorkCar)
Jeep.show_speed()
Mercedes = PoliceCar(speed=115, color="white", name="Mercedes", is_police=True)
Mercedes.show_speed()
Mercedes.turn("налево")
Mercedes.stop()
