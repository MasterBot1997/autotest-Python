# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


# Проверка на ввод числа с ограничением диапозона от 0 до 100.000
# не включая крайние границы диапозона
def check_number(nu):
    while True:
        if nu.isnumeric():
            if int(nu) > 0 and int(nu) < 100000:
                return nu
        print("Вы ввели некорректное значение, попробуйте еще раз!")
        nu = input("Введите число: ")

# Проверка является ли число простым
def prime_number_checking(n):
    # Создаем переменную делителя для проверки переданного числа на простоту
    d = 2
    while int(n) % d != 0:
        # увеличиваем делитель до момента пока остаток от деления не будет равен 0
        d+=1
    # Проверяем делитель по завершению цикла, если делитель и переданное значенияе равны
    # значит до введенного числа оно не делилось на другие без остатка, получается число просто
    # и передаем булевое значение "правда", в ином случае "ложь"
    if int(n) == d: return True
    return False


print("Число должно быть в диапазоне от 0 до 100.000")
number = check_number(input("Введите число которое хотите проверить, является ли оно простым: "))

if prime_number_checking(number): print('Число', number, 'является простым', sep=' ')
else: print('Число', number, 'не является простым', sep=' ')