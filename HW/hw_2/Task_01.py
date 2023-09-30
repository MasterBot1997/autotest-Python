# Решить 6 задачу семинара.

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# MULTIPLE_OF_FACE_VALUE = 50
import constant


def main():
    interface_user()


# ✔ Допустимые действия: пополнить, снять, выйти
def interface_user():
    account_balance = 0
    count = 1
    while True:
        print(f"Баланс вышего счета {account_balance}\n")
        num_type = input(
            "Введите номер действия которое хотите выполнить:\n"
            "1 - Пополнить баланс\n"
            "2 - Снять деньги\n"
            "3 - Выйти\n"
        )
        match num_type:
            case "1":
                account_balance = wealth_test(account_balance)
                account_balance = replenishment_of_balance(account_balance)
            case "2":
                account_balance = wealth_test(account_balance)
                result = withdraw_money(account_balance)
                if not isinstance(result, str):
                    account_balance = result
                else:
                    print(result)
            case "3":
                break
            case _:
                # print('Вы ввели несуществующую операцию, попробуйте еще раз')
                print(account_balance)

        # Тут расположен счетчик который начисляет 3% после каждой 3 операции
        if count < 3:
            count += 1
        else:
            count = 1
            account_balance = interest_on_the_balance(account_balance)


# Функция пополнения баланса ------ (Подскажите какой вариант записи с точки зрения кода лучше, тот что закомменитирован или тот что активен?)
def replenishment_of_balance(balance):
    print("Сумма для пополнения баланса должна быть кратна 50!")
    # money_amount = multiplicity_check(input('Введите сумму на которую хотите пополнить баланс: '))
    # return balance + money_amount
    return balance + multiplicity_check(
        input("Введите сумму на которую хотите пополнить баланс: ")
    )


# Функция снятия суммы с баланса
def withdraw_money(balance):
    print("Сумма для того чтобы снять деньги сумма не должа быть больше остатка на счете и должна быть кратна 50!")
    value = checking_the_amount(multiplicity_check(input("Введите сумму которую хотите снять: ")), balance)
    if value == 0:
        return 0
    if value + commission_calculation(value) > balance:
        return "Сумма которую вы хотите снять с учетом кимиссии превышает сумму остатка на счете"
    return balance - value - commission_calculation(value)


# функция расчета процента комиссии
def commission_calculation(value):
    commissions = value * 1.5 / 100
    if commissions < 30:
        return 30
    elif commissions > 600:
        return 600
    return commissions


# Функция проверки введенной суммы
def multiplicity_check(value):
    while True:
        if value.isnumeric() and int(value) % constant.MULTIPLE_OF_FACE_VALUE == 0:
            return int(value)
        print("Сумма не кратна 50, попробуйте еще раз!")
        value = input("Введите сумму кратную 50: ")


# Проверка суммы при снятии что она не превышает сумму остатка
def checking_the_amount(value, balance):
    while value > balance:
        print("Сумма превышает остаток на балансе, попробуйте еще раз!")
        value = multiplicity_check(input("Введите сумму не превышающую остаток на балансе: "))
    else:
        return value


# Функция начисления процентов
def interest_on_the_balance(balance):
    return balance + balance * 0.03


# Проверка на богатство
def wealth_test(balance):
    if balance > 5000000:
        return balance - (balance * 0.1)
    return balance


main()
