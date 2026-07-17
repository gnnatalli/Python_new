"""07 Сравнение матриц

Напишите программу, которая
- обрабатывает две квадратные матрицы одинакового размера
- и проверяет, совпадают ли их диагональные элементы.

Данные:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 0, 3],
    [0, 5, 0],
    [7, 0, 9]
]

Пример вывода:
Совпадают ли главные диагонали: True
Совпадают ли побочные диагонали: True
"""

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 0, 3],
    [0, 5, 0],
    [7, 0, 9]
]

n = len(matrix1)

diag1_matrix1 = []
diag1_matrix2 = []

for i in range(n):
    diag1_matrix1.append(matrix1[i][i])
    diag1_matrix2.append(matrix2[i][i])

diag2_matrix1 = []
diag2_matrix2 = []

for i in range(n):
    diag2_matrix1.append(matrix1[i][n - 1 - i])
    diag2_matrix2.append(matrix2[i][n - 1 - i])

print("Совпадают ли главные диагонали:", diag1_matrix1 == diag1_matrix2)
print("Совпадают ли побочные диагонали:", diag2_matrix1 == diag2_matrix2)