# a = 123
# b = 1.8
# c = 'Hello'
# print(a, b, c)
# print(a, '-', b, '-', c)
# print('{} - {} - {}'.format(a, b, c))
# print(f'{a} - {b} - {c}')
# def max_num(a, b):
#     if a > b:
#         return a
#     return b
# def quick_sort(array): # быстрая сортировка
#     if len(array) <= 1: # условие выхода из рекурсии
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot] # генератор списка для 1 массива
#     print(less)
#     greater = [i for i in array[1:] if i >= pivot] # генератор списка для 2 массива
#     print(greater)
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([10, 5, 2, 3]))
import random
import time


# def merge_sort(num):  # сортировка слиянием
#     if len(num) > 1:
#         mid = len(num) // 2 # делим массив надвое, пока не останется по одному элементу
#         left = num[:mid]
#         right = num[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i, j, k = 0, 0, 0
#         while i < len(left) and j < len(right): # сравниваем между списками по 2 значения и добавляем в num[k]
#             if left[i] < right[j]:
#                 num[k] = left[i]
#                 i += 1
#             else:
#                 num[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left): # если после сравнения остались значения, добавляем их в конец двумя циклами
#             num[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             num[k] = right[j]
#             j += 1
#             k += 1
# list_1 = [12, 3, 4, 5, 8, 9, 7]
# merge_sort(list_1)
# print(list_1)

# 31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# def fib(n): # функция принимает число n
#     if n == 0:
#         return 0 # 1 элемент
#     elif n == 1:
#         return 1 # 2 элемент
#     else:
#         return fib(n - 1) + fib(n - 2) # функция постоянно будет возвращаться к 0 и 1 элементу из них форм-ть след.элементы
# print(fib(5))

# Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# 1 вариант
# array = [int(input('введите оценку: ')) for _ in range(int(input('введите кол-во оценок: ')))]
# print(array)
# max_num = max(array)
# min_num = min(array)
# for i in range(len(array)):
#     if array[i] == max_num:
#         array[i] = min_num
# print(array)

# 2 вариант
# array = [int(input('введите оценку: ')) for _ in range(int(input('введите кол-во оценок: ')))]
# print(array)
# max_num = array[0]
# min_num = array[0]
# for i in array:
#     if i < min_num:
#         min_num = i
#     if i > max_num:
#         max_num = i
# for i in range(len(array)):
#     if array[i] == max_num:
#         array[i] = min_num
# print(array)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# 1 вариант
# def simple_num(n):
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             return 'Число не является простым'
#     return 'Число является простым'
# print(simple_num(14))

# 2 вариант (наиболее лаконичный, но не соответствует условию задачи: Напишите функцию)
# n = int(input('n: '))
# for i in range(2, n // 2 + 1): # т.к. самый большой целый делитель числа это число пополам
#     if n % i == 0:
#         print('Число не является простым')
#         break
# else:
#     print('Число является простым')

# 3 вариант
# n = int(input('n: '))
# flag = False
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         print('Число не является простым')
#         flag = True
#         break
# if not flag:
#     print('Число является простым')

# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def exponentiation(a, b):
#     if b == 1:
#         return a
#     return a * exponentiation(a, b - 1)
# a = int(input('A: '))
# b = int(input('B: '))
# print(exponentiation(a, b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b) + 1
a = int(input('a: '))
b = int(input('b: '))
print(sum(a, b))
