
# Практическое задание
# 1. Поработайте с переменными, создайте несколько, выведите на экран."
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
print("1. Поработайте с переменными, создайте несколько, выведите на экран.")

number = 2
number_Pi = 3.14159265358979323846
isItFact = True
my_Name = "Александр"
en_Dict = {"Dog": "Собака"}
discipline = ("Семь", "раз", "отмерь", "1", "раз", "отрежь")
novelette = [
                ["Снова"],
                [
                    ["выкуриваю свою самую последнюю сигарету"],
                    ["выпиваю последний бокал вина вечером"],
                    ["пропускаю свою первую тренировку"]
                ]
            ]
_all = number, number_Pi, isItFact, my_Name, en_Dict, discipline
for i in _all:
    print(">>", i, "<<", 'соответствует типу переменной -', type(i))
