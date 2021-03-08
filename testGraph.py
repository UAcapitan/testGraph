import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import copy
import math
from tkinter import *
import sys

# Инициализация графа
graph = nx.Graph()

x = 26

arr = [
    [0,645,868,125,748,366,256,316,1057,382,360,471,428,593,311,844,602,232,575,734,521,120,343,312,396],
    [645,0,252,664,81,901,533,294,394,805,975,343,468,196,957,446,430,877,1130,213,376,765,324,891,672],
    [868,252,0,858,217,1171,727,520,148,1111,1221,611,731,390,1045,591,706,1100,1391,335,560,988,547,1141,867],
    [125,664,858,0,738,431,131,407,1182,257,423,677,557,468,187,803,477,298,671,690,624,185,321,389,271],
    [748,81,217,738,0,1119,607,303,365,681,833,377,497,270,925,365,477,977,1488,287,297,875,405,957,747],
    [366,901,1171,431,1119,0,561,618,1402,328,135,747,627,898,296,1070,908,134,280,1040,798,246,709,143,701],
    [256,533,727,131,607,561,0,298,811,388,550,490,489,337,318,972,346,427,806,478,551,315,190,538,149],
    [316,294,520,407,303,618,298,0,668,664,710,174,294,246,627,570,506,547,883,387,225,435,126,637,363],
    [1057,394,148,1182,365,1402,811,668,0,1199,1379,857,977,474,1129,739,253,1289,1539,333,806,1177,706,1292,951],
    [382,805,1111,257,681,328,388,664,1199,0,152,780,856,725,70,1052,734,159,413,866,869,263,578,336,949],
    [360,975,1221,423,833,135,550,710,1379,152,0,850,970,891,232,1173,896,128,261,1028,1141,240,740,278,690],
    [471,343,611,677,377,747,490,174,857,780,850,0,120,420,864,282,681,754,999,556,51,590,300,642,640],
    [428,468,731,557,497,627,489,294,977,856,970,120,0,540,741,392,800,660,1009,831,171,548,420,515,529],
    [593,196,390,468,270,898,337,246,474,725,891,420,540,0,665,635,261,825,1149,141,471,653,279,892,477],
    [311, 957,1045,187,925,296,318,627,1129,70,232,864,741,665,0,1157,664,162,484,805,834,193,508,331,458],
    [844,446,591,803,365,1070,972,570,739,1052,1173,282,392,635,1157,0,896,1097,1363,652,221,964,696,981,1112],
    [602,430,706,477,477,908,346,506,253,734,896,681,800,261,664,896,0,774,1138,190,732,662,540,883,350],
    [232,877,1100,298,977,134,427,547,1289,159,128,754,660,825,162,1097,774,0,338,987,831,112,575,176,568],
    [575,1130,1391,671,1488,280,806,883,1539,413,261,999,1009,1149,484,1363,1138,338,0,1299,1065,455,984,444,951],
    [734,213,335,690,287,1040,478,387,333,866,1028,556,831,141,805,652,190,987,1299,0,576,854,420,1036,608],
    [521,376,560,624,297,798,551,225,806,869,1141,51,171,471,834,221,732,831,1065,576,0,641,351,713,691],
    [120,765,988,185,875,246,315,435,1177,263,240,590,548,653,193,964,662,112,455,854,641,0,463,190,455],
    [343,324,547,321,405,709,190,126,706,578,740,300,420,279,508,696,540,575,984,420,351,463,0,660,330],
    [312,891,1141,389,957,143,538,637,1292,336,278,642,515,892,331,981,883,176,444,1036,713,190,660,0,695],
    [396,672,867,271,747,701,149,363,951,949,690,640,529,477,458,1112,350,568,951,608,691,455,330,695,0]
]

# Города
citys = ['Вінниця', 'Дніпро', 'Донецьк', 'Житомир', 'Запоріжжя', 'Івано-Франківськ', 'Київ', 'Кіровоград',
         'Луганськ', 'Луцьк', 'Львів', 'Миколаїв', 'Одесса', 'Полтава', 'Рівне', 'Сімферопіль', 'Суми', 
         'Тернопіль', 'Ужгород', 'Харків', 'Херсон', 'Хмельницький', 'Черкаси', 'Чернівці', 'Чернігів']

# Найти куда идти

def name_in_int():
    global x1, x2, x3, arr
    try:
        x1 = entry_1.get()
        x2 = entry_2.get()

        name = x1
        namex = x2

        if x1 in citys:
            x1 = citys.index(x1) + 1
        else:
            exit

        if x2 in citys:
            x2 = citys.index(x2) + 1
        else:
            exit

        x3 = x1

        arr_save = arr[0]
        arr[0] = arr[x1 - 1]
        arr[x1 - 1] = arr_save
    except:
        sys.exit()

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

    # Обнуление строки
    arr_nums = []

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

    # Функция поиска всех минимумов в списке
    def find_match(myList, element):
        return [i for i, x in enumerate(myList) if x == element]

    # Сколько раз нужно повторить цикл
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

    x1 = 1

    # Переменная с которой нужно сверять
    num = array_min[x2 - 1]

    # Куда идти
    arr_num = []

    # Добавить точку финиша
    arr_num.append(x2)

    
    # Цикл работает до того момента пока num не сравниться с минимальным значением переменной начала
    while num != array_min[x1 - 1]:
        arr_reverse = arr[arr_num[-1] - 1]
        # arr_reverse.reverse()

        len_arr = len(arr_num)

        for i in arr_reverse:
            if array_min[arr_num[-1] - 1] - i in array_min and i != 0:
                indexs_arr = find_match(array_min, array_min[arr_num[-1] - 1] - i)
                indexs_arr.reverse()
                for j in indexs_arr:
                    if arr[j][arr_num[-1] - 1] > 0:
                        arr_num.append(j + 1)
                        break

        if len(arr_num) == len_arr:
            break

    arr_num.append(x3)
    arr_num.reverse()
    del arr_num[1]

    sum_arr = 0
    i = 1
    while i < len(arr_num):
        sum_arr += arr[arr_num[i]-1][arr_num[i-1]-1]
        i += 1

    sum = array_min[x2 - 1]

    if sum_arr != sum:
        # Переменная с которой нужно сверять
        num = array_min[x2 - 1]

        # Куда идти
        arr_num = []

        # Добавить точку финиша
        arr_num.append(x2)

        
        # Цикл работает до того момента пока num не сравниться с минимальным значением переменной начала
        while num != array_min[x1 - 1]:
            arr_reverse = arr[arr_num[-1] - 1]
            arr_reverse.reverse()

            len_arr = len(arr_num)

            for i in arr_reverse:
                if array_min[arr_num[-1] - 1] - i in array_min and i != 0:
                    indexs_arr = find_match(array_min, array_min[arr_num[-1] - 1] - i)
                    indexs_arr.reverse()
                    for j in indexs_arr:
                        if arr[j][arr_num[-1] - 1] > 0:
                            arr_num.append(j + 1)
                            break

            if len(arr_num) == len_arr:
                break

        arr_num.append(x3)
        arr_num.reverse()
        del arr_num[1]

        sum_arr = 0
        i = 1
        while i < len(arr_num):
            sum_arr += arr[arr_num[i]-1][arr_num[i-1]-1]
            i += 1

    i = 0
    while i < len(arr_num):
        arr_num[i] = citys[arr_num[i]-1]
        i += 1

    def build_unique_list_keep_order(seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]
    arr_num = build_unique_list_keep_order(arr_num)
    
    text = ''

    for i in arr_num:
        text += i + ' - '
    
    text = text[:-3]
    
    label_3['text'] = 'Шлях: ' + text

    # Высчитать растояние
    label_4['text'] = 'Відстань між містами: ' + str(sum) + ' км'

# Функция запущенная
def main():
    global time
    if time == 1:
        sys.exit()
    name_in_int()
    algorithm_Dijkstras(arr)
    time += 1

# GUI
root = Tk()
root.title('Navigation')
root.geometry('500x150')
label_1 = Label(root, text='Откуда:')
entry_1 = Entry(root)
label_2 = Label(root, text='Куда:')
entry_2 = Entry(root)
label_3 = Label(root, text='Шлях:')
label_4 = Label(root,text='Відстань між точками:')
button_1 = Button(root, text='Знайти найкоротший шлях', command=main)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
label_2.grid(row=1, column=0)
entry_2.grid(row=1, column=1)
label_3.grid(row=2, column=0, columnspan=2)
label_4.grid(row=3, column=0, columnspan=2)
button_1.grid(row=4, column=0, columnspan=2)

time = 0

root.mainloop()