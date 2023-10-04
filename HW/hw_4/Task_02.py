# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def func(**kwargs):
    dic = {}
    for key, value in kwargs.items():
        if not isinstance(value, (int, float, str, tuple, frozenset)):
            value = str(value)
        dic[value] = key
    return dic

print(func(a=10, b=20, c=30.5, d="hello", e=[1, 2, 3], f={1: 11, 2: 22}))
