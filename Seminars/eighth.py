# with open('seminar_8.txt', 'r', encoding='utf-8') as file:
# text = file.read().splitlines() -> ['Буляша самая прекрасная собака на свете!', 'Буляша самая добрая девочка на Земле!']
# text = file.readlines() -> ['Буляша самая прекрасная собака на свете!\n', 'Буляша самая добрая девочка на Земле!']
# print(text)
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line)
# with open('seminar_8.txt', 'a', encoding='utf-8') as file:
#     some_list = ['солнышко', 'весна', 'хорошенький денёчек']
#     for word in some_list:
#         file.write(word + '\n')
#     print(some_list)
import random

# with open('seminar_8.txt', 'r', encoding='utf-8') as file:
#     find_letter = input()
#     count = 0
#     for letter in file.read():
#         if letter == find_letter:
#             count += 1
#     print(count)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint
# n = int(input('кол-во элементов в списке n: '))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('seminar_8.txt', 'w', encoding='utf-8') as file:
#     for _ in range(randint(1, n)):
#         file.write(str(randint(0, n - 1)) + '\n')
# with open('seminar_8.txt', 'r', encoding='utf-8') as file:
#     mult = 1
#     for ind in file.read().splitlines():
#         mult *= some_list[int(ind)]
# print(mult)

# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки
# в количестве lines (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# 1 вариант (через функцию)
# def read_last(lines, file):
#     if lines > 0:
#         with open(file, 'r', encoding='utf-8') as file_1:
#             text = file_1.read().splitlines()
#             print(text)
#             for line in text[-lines:]:
#                 print(line)
#     else:
#         print('lines < 0')
# print(read_last(5, 'article.txt'))

# 2 вариант (без функции)
# lines = int(input('lines: '))
# if lines > 0:
#     with open('article.txt', 'r', encoding='utf-8') as file:
#         text = file.read().splitlines()
#         print(text)
#         for line in text[-lines:]:
#             print(line)
# else:
#     print('lines < 0')

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).

# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as file_1:
#         text = file_1.read().split()
#         max_word = len(max(text, key=len))
#         text_2 = []
#         for word in text:
#             if len(word) >= max_word:
#                 text_2.append(word)
#         print(text_2)
#
# print(longest_words('article.txt'))




