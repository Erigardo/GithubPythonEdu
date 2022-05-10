# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.


print("***" * 21)
print("Ознакомимся с данными, приведенными ниже")
a = "Выручка от продажи (без НДС)"
# b = "Валовый доход"
c = "Производственные издержки"
d = "Непроизводственные издержки(Реализационные)"
e = "Непроизводственные издержки(Административные)"
data = (a, c, d, e)
for i in data:
    print(i)

money = input("Введите значение для {} в $: ".format(a))
# val = input("Введите значение для {}: ".format(b))
minus_production = input("Введите значение для {} в $: ".format(c))
minus_realisation = input("Введите значение для {} в $: ".format(d))
minus_administration = input("Введите значение для {} в $: ".format(e))

dohod = money
minus = (int(minus_administration)+int(minus_realisation)+int(minus_production))


if money < minus_production+minus_realisation+minus_administration:
    print("Ваш доход в {}$ больше чем расход в {}$".format(dohod, minus))
else:
    print("Ваш расход больше чем доход")
