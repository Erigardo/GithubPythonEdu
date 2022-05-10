# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.

def my_func(a, b, c):
    data = [a, b, c]
    data.sort(reverse=True)
    print(data)
    return data[0] + data[1]


# pop.max
# sorted(reverse=True)

print(my_func(1, 2, 3))
