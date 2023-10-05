from check import check_value


# Пополнение баланса
def replenishment_of_balance(balance):
    value = check_value(input("Введите сумму, на которую хотите пополнить баланс: "))
    balance = int(balance) + int(value)
    return balance


# снятие суммы со счета
def withdraw_cash(balance):
    value = check_value(input("Введите сумму, которую хотите снять: "), balance)
    commission = commission_calculation(int(value))
    if int(value)+commission > balance:
        print('Сумма снятия с учетом комиссии превышает остаток на счете.\nОпервация выполнена не будет')
        return balance
    balance = int(balance) - int(value) - commission
    return balance

# функция расчета процента комиссии
def commission_calculation(value) -> int:
    commissions = value * 1.5 / 100
    if commissions < 30:
        return 30
    elif commissions > 600:
        return 600
    return commissions

# Функция начисления процентов
def interest_on_the_balance(balance):
    balance = balance + balance * 0.03
    return balance

# Проверка на богатство
def wealth_test(balance):
    if balance > 5000000:
        return balance - (balance * 0.1)
    return balance