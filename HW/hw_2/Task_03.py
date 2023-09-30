# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

fraction_1 = input("Введите первую дробь в виде a/b: ")
fraction_2 = input("Введите вторую дробь в виде a/b: ")
numerato_1, denominator_1 = map(int, fraction_1.split("/"))
numerato_2, denominator_2 = map(int, fraction_2.split("/"))


def multiplying_fractions(a,b,c,d):
    return f'{a * c}/{b * d}'

def sum_of_fractions(a,b,c,d):
    new_a = a * d
    new_c = c * b
    new_denominator = d * b
    return f'{new_a + new_c}/{new_denominator}'

print(f'{fraction_1}', ' + ', f'{fraction_2}', ' = ', sum_of_fractions(numerato_1, denominator_1, numerato_2, denominator_2))
print(f'{fraction_1}', ' * ', f'{fraction_2}', ' = ', multiplying_fractions(numerato_1, denominator_1, numerato_2, denominator_2))