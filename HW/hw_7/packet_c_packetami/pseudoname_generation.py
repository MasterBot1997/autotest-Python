# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import choice, randint

GLAS = 'eyuioa'
SOGL = 'qwrtpsdfghjklzxcvbnm'
num_it = randint(4, 7)

def rand_name_file(file: str, count: int):
    with open(file, 'w', encoding='utf-8') as data:
        for _ in range(count):
            answer = [] 
            for _ in range(randint(4, 7)):
                answer.extend([choice(GLAS), choice(SOGL)])
            data.write(f'{"".join(answer).title()[:num_it]}\n')



if __name__ == '__main__':
    rand_name_file('file_test/task_02.txt', 7)

    