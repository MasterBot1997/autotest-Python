# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# Функция проверки остатка для замены на соответствующее буквенное значение
def checking_the_remainder_of_the_division(num):
    if num == 10:
        return "a"
    elif num == 11:
        return "b"
    elif num == 12:
        return "c"
    elif num == 13:
        return "d"
    elif num == 14:
        return "e"
    elif num == 15:
        return "f"
    else:
        return num

# Константа делителя для избежания магического числа
DEl = 16
number = int(input("Введите число: "))
res = ''
print(hex(number))

while number:
    res = f"{checking_the_remainder_of_the_division(number%DEl)}" + res
    number //= DEl

print(res)