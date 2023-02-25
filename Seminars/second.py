# 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# n = int(input('Введите значение n: '))
# factorial = 1
# i = 2
# while i <= n:
#     factorial *= i
#     i += 1
# print(factorial)

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1
# 0,1,1,2,3,5,8,13...

# first_el = 0
# second_el = 1
# number = int(input('Введите число: '))
# next_el = first_el + second_el
# i = 3
# while next_el < number:
#     first_el = second_el
#     second_el = next_el
#     next_el = first_el + second_el
#     i += 1
# if next_el == number:
#     print(i)
# else:
#     print(-1)

# 13. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная
# температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# max_count = 0
# count = 0
# n = int(input('Введите количество рассматриваемых дней: '))
# for _ in range(n):
#     temp = int(input())
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# if max_count == 0 and count != 0:
#     print(count)
# else:
#     print(max_count)

# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# Д/З

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2
# пользователь будет вводить каждое число на новой строке для задач 10, 12.

# count = 0
# n = int(input('n: '))
# for _ in range(n):
#     temp = int(input())
#     if temp == 1:
#         count += 1
# print(count if count < n/2 else n - count)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# s = int(input('s: '))
# p = int(input('p: '))
# x = 0
# y = 1
# for x in range(s):
#     for y in range(p):
#         if x + y == s and x * y == p:
#             print(x, y)
#         else:
#             x += 1
#             y += 1

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
# n = int(input('n: '))
# num_exp = 1
# while num_exp < n:
#     if (num_exp * 2 > n):
#         break
#     else:
#         num_exp = num_exp * 2
#     print(num_exp)