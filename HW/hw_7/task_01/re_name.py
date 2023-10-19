import os
from pathlib import Path
from posixpath import abspath
from random import randint

FORMAT_LIST = [
    ".jpg",
    ".png",
    ".bmp",
    ".gif",
    ".tif",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".pdf",
    ".mp3",
    ".wav",
    ".midi",
    ".aac",
    ".html",
    ".htm",
    ".mht",
]


def rename_file(
    path_dir: str, # в этом параметре передаем путь до рабочей папки
    new_name: str = "", # параметр содержащий новое имя
    ot: int=0, # начало среза со старого имени
    last: int=5, # конец среза со старого имени
    form: str=f'{FORMAT_LIST[randint(0, len(FORMAT_LIST)-1)]}' # передаем расширение файла, 
                                                               # если не указываем получаем рандомное
):
    dir_list = check_dir(os.listdir(path_dir))

    # в цикле создаем новое имя и сразу перезаписывапем старое имя файла на новое
    for i in range(len(dir_list)):
        name = f'{dir_list[i].split(".")[0][ot:last:]}{new_name}_{i+1}{form}'
        os.rename(dir_list[i], name)

# Выполняем проверку содержимого дериктории 
# по итогу которой в списке остаются только имена файлов
def check_dir(dir_list: list):
    os.chdir("./test_folder/")
    for i in range(len(dir_list)):
        if not os.path.isfile(dir_list[i]):
            dir_list.pop(i)
    return dir_list



if __name__ == '__main__':
    path_test = "./test_folder/"
    rename_file(path_dir=path_test, new_name='boby_smile', ot=2, last= 6, form='.bin')

