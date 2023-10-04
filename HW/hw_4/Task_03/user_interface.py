from main import *

# ✔ Допустимые действия: пополнить, снять, выйти
def interface_user():
    account_balance = 0
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
                pass
            case "2":
                pass
            case "3":
                break
            case _:
                # print('Вы ввели несуществующую операцию, попробуйте еще раз')
                print(account_balance)