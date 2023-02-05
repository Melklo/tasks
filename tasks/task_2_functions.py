'''
Задание 2.
Функции, методы, тайпинги.
'''

from typing import Tuple, Optional, Union

# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def reverse(string: str) -> str:
    rev = ''
    for i in range(len(string) - 1, -1, -1):
        rev += string[i]
    return rev


print(reverse('Hello World mtf'))


# Реализовать фунекцию, которая принимает два параметра: число и степень - и возвращает это число,
# возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.

def sol(number: int, pow: int = 2) -> int:
    return number ** pow


print(sol(2))


# Реализовать функцию, которая принимает произвольный набор параметров и возвращает кортеж, содержащий
# типы переданных параметров.

def types(*args):
    for arg in range(len(args)):
        if arg < len(args):
            print (type(arg))
        break
    return arg


print(types('1', "str", 1.3, 1))


# Реализовать функцию, которая принимает произвольный набор именованных параметров и возвращает их
# группировку по типу в виде словаря.
# Например, если входные параметры заданы как `a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0`,
# то необходимо вернуть словарь следующего вида:
# {
#   int: [['a', 34], ['c', 2]],
#   str: [['b', 'some text']],
#   float: [['d', 1.3], ['f', -3.0]],
#   dict: [['e', {1: 2}]]
# }
def sort_type(**kwargs):
    answer = kwargs.fromkeys(['int', 'str', 'float', 'dict'])
    i_n = []
    s = []
    f = []
    d = []
    for i in kwargs:
        if type(kwargs[i]) == int:
            i_n += ([i, kwargs[i]],)
            answer['int'] = i_n
        if type(kwargs[i]) == str:
            s += ([i, kwargs[i]],)
            answer['str'] = s
        if type(kwargs[i]) == float:
            f += ([i, kwargs[i]],)
            answer['float'] = f
        if type(kwargs[i]) == dict:
            d += ([i, kwargs[i]],)
            answer['dict'] = d
    return answer


print(sort_type(a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0))


# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.
def function(text: str, *arg, **kwargs) -> str:
    my_list = text.split("*")
    for i in range(len(my_list)):
        line = my_list[i]
        if i % 2:
            if not line:
                my_list[i] = "*"
            elif line in kwargs:
                my_list[i] = str(kwargs[line])
            else:
                try:
                    my_list[i] = str(arg[int(line)])
                except (ValueError, IndexError):
                    return "Wrong data!"

    result = "".join(my_list)
    return result


