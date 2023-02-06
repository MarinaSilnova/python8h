#В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.
import random 
rows = 5
columns = 30
numbers = [None]*rows
for index in range(len(numbers)):
    numbers[index] =[random.randint(10,30) for _ in range(columns)]

numbers[0] =[random.randint(10,30) for _ in range(31)]
numbers[1] =[random.randint(10,30) for _ in range(30)]
numbers[2] =[random.randint(10,30) for _ in range(31)]
numbers[3] =[random.randint(10,30) for _ in range(31)]
numbers[4] =[random.randint(10,30) for _ in range(30)]

for el in numbers:
    print(el)


sum_rows_max=0
min_j = 0

for i in range(rows):    
    for j in range(columns-7):
        a = numbers[i][j:j+7]
        sum_rows = sum(a)
        if sum_rows > sum_rows_max:
            sum_rows_max=sum_rows
            max_j = j
    print(f'В {i+5} месяце прошлого года самый жаркий период с  {max_j + 1} по  {max_j + 8} число // ({round(sum_rows_max/7, 2)}) ')
    
for i in range(rows):    
    sum_rows_min=sum(numbers[i][0:7])
    for j in range(columns-7):
        sum_rows = sum(numbers[i][j:j+7])
        if sum_rows < sum_rows_min:
            sum_rows_min=sum_rows
            min_j = j
    print(f'В {i+5}  месяце прошлого года самый холодный период  с  {min_j + 1} по  {min_j + 8} число // ({round(sum_rows_min/7, 2)}) ')
    
