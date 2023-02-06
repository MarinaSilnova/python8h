#В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу.
#  Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random

rows = 4
columns = random.randint(20,30)

numbers = [None]*rows
used = [numbers[0]]

for index in range(len(numbers)):
    numbers[index] =[random.randint(1,10) for _ in range(columns)]

for el in numbers:
    print(el)

avg_max = 0
max_i = 0
for i in range(rows):    
    avg = sum(numbers[i])/len(numbers[i])
    print(round(avg, 2))
    if avg_max < avg:
        avg_max = avg
        max_i = i
print(f' Группa номер {max_i+1} с наилучшим средним баллом {round(avg_max, 2)} ')
