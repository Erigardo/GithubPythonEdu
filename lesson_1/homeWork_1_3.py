# 3.Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_setNumber = input('Введите число: ')
a = int(user_setNumber)
b_str = (str(a)+str(a))
c_str = (str(a)+str(a)+str(a))
b = int(b_str)
c = int(c_str)
_abc = ["сложим >>>", a,  '+', b,  '+', c, 'получим >>>']
sumM_abc = a + b + c
for i in _abc:
    print(i)
print(sumM_abc)
