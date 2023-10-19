from pathlib import Path
from random import randint, uniform

def add_text(count: int, file: str):
    NUM_MAX = 1000
    NUM_MIN = -1000
    with open(file, 'w', encoding='utf-8') as data:
        for _ in range(count):
            data.write(f'{randint(NUM_MIN, NUM_MAX)}|{uniform(NUM_MIN, NUM_MAX)}\n')


if __name__ == '__main__':
    add_text(5, f'{Path().cwd()}/task_01.txt')