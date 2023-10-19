# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42

# Имя файла и его размер должны быть в рамках переданного диапазона.

from string import ascii_lowercase, digits
from random import choices, randint

path_folder = "file_test/task_04/"


def func_2(
    path: str,
    count: int = 5,
    ext: str = "txt",
    min_name: int = 6,
    max_name: int = 30,
    min_size: int = 256,
    max_size: int = 4096,
):
    for _ in range(count):
        my_data = bytes(randint(0, 255) for i in range(randint(min_size, max_size)))
        name_of_file = "".join(
            choices(ascii_lowercase + digits, k=randint(min_name, max_name))
        )

        with open(f"{path + name_of_file}.{ext}", "wb") as data:
            data.write(my_data)


def new_func(**kwargs):
    for ext, count in kwargs.items():
        func_2(ext, count=count)

if __name__ == "__main__":
    path_folder = "file_test/task_04/"
    func_2(path_folder, count=10)
    new_func(txt=1, bin=2)
