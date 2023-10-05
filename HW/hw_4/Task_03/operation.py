
def replenishment_of_balance(balance):
    value = input('Введите сумму, которую хотите снять: ')
    balance = balance + value
    return balance

def withdraw_cash(balance):
    value = input('Введите сумму, которую хотите снять: ')
    balance = balance - value
    return balance