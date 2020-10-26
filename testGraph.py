import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import copy
import math

# Инициализация графа
graph = nx.Graph()

# Запрос у пользователя сколько графов
print('Сколько вершин у вас?')
x = int(input())

# Если у графа меньше 3 вершин, то прекратить работу
if x < 3:
    print('Введите 3 или больше вершины.')
    while x < 3:
        x = int(input())

x = x + 1

# Запрос у пользователя матрицы весов
print('Введите матрицу весов. Числа вводите через один пробел.')
print('Если ребра нету, то пишите 0.')
text = '   '
arr = []
for i in range(1,x):
   text = text + 'X'+str(i)+' '

print(text)

for i in range(1,x):
    num_in_array = input('X'+str(i)+' ')
    a = num_in_array.split(' ')
    arr.append(a)

# Создание вершин графа
for i in range(1,x):
    graph.add_node('X'+str(i))

# Создание ребёр и их весов
weight = []

for i in range(0,x - 1):
    for j in range(0,x - 1):
        if int(arr[i][j]) != 0:
            weight_element = ('X'+str(i+1),'X'+str(j+1),arr[i][j])
            weight.append(weight_element)

graph.add_weighted_edges_from(weight)

# Алгоритм Дейкстры
def algorithm_Dijkstras(arr):
    infinity = math.inf

    # Массив кратких путей
    arr_all = []

    # Указываю строку
    arr_nums = []

    # Задаю X1 - X1
    arr_nums.append(0)

    # Задаю первую строку
    while len(arr_nums) < len(arr[0]):
        arr_nums.append(infinity)

    # Добавить строку в общий список
    arr_all.append(arr_nums)

    # Найти минимальное число
    min_arr = min(arr_all[0])

    # Обнуление строки
    arr_nums = []

    # Первый элемент второго столбца
    arr_nums.append(None)

    # Цикл для второго столбца
    for i in range(1,len(arr[0])):

        if int(arr[0][i]) == 0:
            arr_nums.append(infinity)
        elif min_arr + int(arr[0][i]) < arr_all[0][i]:
            arr_nums.append(min_arr+int(arr[0][i]))
        else:
            arr_nums.append(infinity)

    # Найти минимум в массиве где есть None
    def min_None(arr):

        arr_None = []
        for el in arr:
            if el == None:
                arr_None.append(infinity)
            else:
                arr_None.append(el)
        min_N = min(arr_None)
        return min_N

    def find_match(myList, element):
        return [i for i, x in enumerate(myList) if x == element]

    # Сколько раз нужно полторить цикл
    i_repeat = len(arr[0]) - 3

    i_arr = 0

    # Довавление новых столбиков
    while i_arr <= i_repeat:

        min_arr = min_None(arr_all[-1])

        # Поиск минимумов
        arr_min = find_match(arr_all[-1],min_arr)

        # Сделать цикл для повторяющихся минимальных значений в списке
        j_arr = 0

        for i_min in arr_min:

            arr_nums = []

            for i in range(0,len(arr[0])):
                
                if arr_all[-1-j_arr][i] == None:
                    arr_nums.append(None)
                elif arr_all[-1-j_arr][i] == min_arr:
                    arr_nums.append(None)
                elif int(arr[i_min][i]) == 0:
                    arr_nums.append(infinity)
                elif int(min_arr + int(arr[i_min][i])) <= arr_all[-1][i]:
                    arr_nums.append(min_arr + int(arr[i_min][i]))
                else:
                    arr_nums.append(arr_all[-1 - j_arr][i])

                if arr_all[-1-j_arr][i] != None and arr_nums[i] != None:
                    if arr_all[-1-j_arr][i] < arr_nums[i]:
                        arr_nums[i] = arr_all[-1-j_arr][i]
            
            arr_all.append(arr_nums)

            j_arr += 1
        i_arr += 1

    # Список со всеми краткими дорогами от X1
    array_min = []

    i = 0
    j = 0

    # Добавление самых кратких путей в список
    while i < len(arr):
        arr_min = []
        j = 0
        while j <= len(arr[0]) - 2:
            arr_min.append(arr_all[j][i])
            j += 1
        i += 1
        array_min.append(min_None(arr_min))

    # Вывести все пути
    i = 0
    while i < len(array_min):
        print('X1 - X', i + 1, ' = ', array_min[i])
        i += 1

algorithm_Dijkstras(arr)

# Визуализация графа
nx.draw(graph,node_color='green',node_size=1000,with_labels=True)
plt.draw()
plt.show()