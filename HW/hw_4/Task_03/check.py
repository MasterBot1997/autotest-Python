def check_value(value=0, balance=0):
    while True:
        if value.isdigit() and int(value) % 50 == 0:
            if balance:
                if int(value) <= int(balance):
                    return value
                else:
                    print("Сумма для снятия превышает остаток на счете.")
            else:
                return value
        value = input("Вы ввели некорректное значение\nПопробуйте еще раз: ")
