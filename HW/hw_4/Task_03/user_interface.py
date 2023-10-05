from operation import *

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
        if num_type == '1' or num_type == '2':
            print('Сумма для пополнения и снятия должна быть кратной 50!')
            account_balance = wealth_test(account_balance)
        match num_type:
            case "1":
                account_balance = replenishment_of_balance(account_balance)
            case "2":
                account_balance = withdraw_cash(account_balance)
            case "3":
                break
            case _:
                print('Вы ввели несуществующую операцию, попробуйте еще раз')
        
        # Тут расположен счетчик который начисляет 3% после каждой 3 операции
        if count < 3:
            count += 1
        else:
            count = 1
            account_balance = interest_on_the_balance(account_balance)
