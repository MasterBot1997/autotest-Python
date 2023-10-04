# Функция транспонирования матрицы
def matrix_transpose(matrix):
    new_mat = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        new_mat.append(temp)
    return new_mat

# Функция проверки правильности матрицы
def check_matrix(matrix):
    for i in matrix:
        for j in matrix:
            if len(i) != len(j):
                return False
    return True


# варианты матриц с разнам количеством столбцов и колонн и одной неверной матрицей
my_matrix = [[1, 2, 3], [4, 5, 6]]
# my_matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# my_matrix = [[1, 2, 3], [4, 5, 6], [7]]

# new_matrix = matrix_transpose(my_matrix)

if check_matrix(my_matrix):
    new_matrix = matrix_transpose(my_matrix)
    # Два цикла печати старой и новой матрицы для проверки в консоли
    for i in my_matrix:
        print(i)
    for i in new_matrix:
        print(i)
else:
    print("Матрица должна быть с равным количеством данных в каждой строке")
