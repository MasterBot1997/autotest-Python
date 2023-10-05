from check import check_value


# Пополнение баланса
def replenishment_of_balance(balance):
    value = check_value(input("Введите сумму, на которую хотите пополнить баланс: "))
    balance = int(balance) + int(value)
    return balance


# снятие суммы со счета
def withdraw_cash(balance):
    value = check_value(input("Введите сумму, которую хотите снять: "), balance)
    balance = int(balance) - int(value)
    return balance
