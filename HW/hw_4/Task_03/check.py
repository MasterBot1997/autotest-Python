def check_value(value):
    while True:
        if value.isdigit() and value % 50 == 0:
            return value
        value = input("Вы ввели некорректное значение\nПопробуйте еще раз: ")
