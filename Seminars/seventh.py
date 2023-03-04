# 1 вариант
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
# print(res)
import math
import time

# 2 вариант через lambda функции
# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Функция map
# data = '12 13 8 52 43 18 14'
# print(data)
# print(type(data))
# data = list(map(int, data.split()))
# print(data)
# print(type(data))

# Функция filter
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# 2 вариант через lambda функции с применением функций map и filter
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

some_list = [1, 5, 15, 98, 3, 6]
# for ind in range(len(some_list)):
#     some_list[ind] = str(some_list[ind])
# print(some_list) # -> ['1', '5', '15', '98', '3']
# print(type(some_list))
#
# new_list = list(map(str, some_list)) # map принимает 2 параметра: колбэк функции, кот. хотим применить ко всем объектам, и сам объект
# print(new_list) # -> ['1', '5', '15', '98', '3']
# print(type(new_list))
# def even(x):
#     return x % 2 == 0

# new_list = list(filter(even, some_list))

# new_list = list(filter(lambda x: x % 2 == 0, some_list))
# print(list(enumerate(some_list)))

# for ind, value in enumerate(some_list):
#     print(ind, value)
# for ind in range(len(some_list)):
#     print(ind, some_list[ind])

# first_list = ['apple', 'orange', 'grape']
# second_list = ['яблоко', 'апельсин', 'виноград']
# for eng, ru in zip(first_list, second_list):
#     print(eng, ru) # -> apple яблоко orange апельсин grape виноград

# 47. У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество раз):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transormed_values = list(map(transformation, values))
# print(list(map(transformation, values)))

# Задача №49. Решение в группах Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой
# имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой
# вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой
# планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс
# в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна.

# import math
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# new = list(filter(lambda x: x[0] != x[1], orbits))
# new2 = max(map(lambda x: x[0] * x[1] * math.pi, new))
# print(list(filter(lambda x: x[0] * x[1] * math.pi == new2, new)))
# print(max(list(map(lambda x: x[0] * x[1] * math.pi, filter(lambda x: x[0] != x[1], orbits)))))

# Задача №51. Решение в группах Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и
# вычисляет его характеристику.
# def same_by(characteristic, objects):
#     if len(objects) == 0:
#         return True
#     for i in range(len(objects)):
#         if characteristic(objects[i]) != characteristic(objects[0]):
#             return False
#     return True
# values = [0, 2, 10, 6, 7]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# Дан массив с числами, и целевое значение. Нужно проверить найдутся ли в массиве два числа, чья сумма равна целевому значению

# some_list = [90, 19, 48, 24, 12]
# summa = 102
# 1 вариант
# start = time.perf_counter()
# for i in some_list:
#     if summa - i in some_list:
#         print('yes')
#         break
# else:
#     print('no')
# end = time.perf_counter()
# print(end - start)
# 2 вариант (оптимальный по скорости выполнения)
# start = time.perf_counter()
# some_set = set(some_list)
# for i in some_set:
#     if summa - i in some_set:
#         print('yes')
#         break
# else:
#     print('no')
# end = time.perf_counter()
# print(end - start)

# Д/З

# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# # насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# # (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# # то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# # В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# text = 'пара-ра-рам рам-пам-папам па-ра-па-да'
# def rhythm_in_poetry(text):
#     list = text.split()
#     characteristic = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
#     temp = characteristic(list[0])
#     if all([characteristic(i) == temp for i in list]):
#         return 'Парам пам-пам'
#     return 'Пам парам'
# print(rhythm_in_poetry(text))

# Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows = 6, num_columns = 6):

    for i in range(1, num_rows + 1):
        list = []
        for j in range(1, num_columns + 1):
            list.append(str(operation(i, j)))
        print(" ".join(list))

print_operation_table(lambda x, y: x * y)
