from logger import logger
from datetime import datetime

from constant import *


def main():
    interface_user()


# ✔ Допустимые действия: пополнить, снять, выйти
def interface_user():
    account_balance = 0
    count = 1
    while True:
        logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Баланс счета {account_balance}\n')
        num_type = input(
            "Введите номер действия которое хотите выполнить:\n"
            "1 - Пополнить баланс\n"
            "2 - Снять деньги\n"
            "3 - Выйти\n"
        )
        match num_type:
            case "1":
                logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Выбрана операция пополнения счета')
                # проверка на богатство
                account_balance = wealth_test(account_balance)
                # Пополнение баланса
                account_balance = replenishment_of_balance(account_balance)

            case "2":
                logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Выбрана операция снятия денег со счета')
                account_balance = wealth_test(account_balance)
                result = withdraw_money(account_balance)
                if not isinstance(result, str):
                    account_balance = result
                else:
                    logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - {result}')
            case "3":
                logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - завершение работы программы')
                break
            case _:
                logger.warning(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Введена несуществующая операция')
                print(account_balance)

        # Тут расположен счетчик который начисляет 3% после каждой 3 операции
        if count < 3:
            logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Выполнена {count} операция')
            count += 1
        else:
            logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Выполнена {count} операция, производится начисление процентов')
            count = 1
            account_balance = interest_on_the_balance(account_balance)


# Функция пополнения баланса ------ (Подскажите какой вариант записи с точки зрения кода лучше, тот что закомменитирован или тот что активен?)
def replenishment_of_balance(balance):
    print("Сумма для пополнения баланса должна быть кратна 50!")
    money_amount = multiplicity_check(input('Введите сумму на которую хотите пополнить баланс: '))
    result = balance + money_amount
    logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Баланс пополнен на сумму {money_amount}')
    return result



# Функция снятия суммы с баланса
def withdraw_money(balance):
    value = checking_the_amount(multiplicity_check(input("Введите сумму которую хотите снять: ")), balance)
    if value == 0:
        return 0
    if value + commission_calculation(value) > balance:
        return "Сумма которую вы хотите снять с учетом кимиссии превышает сумму остатка на счете"
    
    value += commission_calculation(value)
    result = balance - value
    logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - С баланса снята сумма {value}, баланс {result}')
    return result


# функция расчета процента комиссии
def commission_calculation(value):
    commissions = value * 1.5 / 100
    if commissions < LOW_BORDER:
        commissions = LOW_BORDER
        logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - размер комиссии {commissions}')
        return commissions
    elif commissions > HIGH_BORDER:
        commissions = HIGH_BORDER
        logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - размер комиссии {commissions}')
        return commissions
    logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - размер комиссии {commissions}')
    return commissions


# Функция проверки введенной суммы
def multiplicity_check(value):
    while True:
        if value.isnumeric() and int(value) % MULTIPLE_OF_FACE_VALUE == 0:
            return int(value)
        logger.warning(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Сумма {value} не кратна 50.')
        value = input("Введите сумму кратную 50: ")


# Проверка суммы при снятии что она не превышает сумму остатка
def checking_the_amount(value, balance):
    while value > balance:
        logger.warning(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Сумма для снятия {value} превышает сумму на остатке счета {balance}')
        value = multiplicity_check(input("Введите сумму не превышающую остаток на балансе: "))
    else:
        return value


# Функция начисления процентов
def interest_on_the_balance(balance):
    new_balance = balance + balance * 0.03
    logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - на остаток {balance} начислено {balance * 0.03} процентов')
    return new_balance


# Проверка на богатство
def wealth_test(balance):
    if balance > 5000000:
        new_balance = balance - (balance * 0.1)
        logger.info(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Наложен налог на богатство: старый баланс {balance} -> новый баланс {new_balance}')
        return new_balance
    return balance


main()
