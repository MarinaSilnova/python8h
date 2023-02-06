#Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random
rows = 5
columns = 5

numbers = [None]*rows
used = [numbers[0]]

for index in range(len(numbers)):
    numbers[index] =[random.randint(1,30) for _ in range(columns)]

for el in numbers:
    print(el)
sum_diagonal = 0
for i in range(rows):
    for j in range(columns):
        if i==j:
            sum_diagonal += numbers[i][j]
print(f'Cуммa главной диагонали матрицы = {sum_diagonal}')
for i in range(rows):    
    sum_rows = sum(numbers[i])
    if sum_rows > sum_diagonal:
        print(f'сумма элементов строки номер {i} = {sum_rows} -  превосходит сумму главной диагонали матрицы ')
        