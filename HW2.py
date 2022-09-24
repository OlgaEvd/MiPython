# ЗАДАЧА 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# num = float(input("Введите число:"))
# def sumNum(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum

# print(f"Сумма цифр = {sumNum(num)}")


# задача 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# num = int(input("Введите число N:"))
# def product(num):
#     if num == 1:
#         return 1
#     else:
#         return num * product(num - 1)

# list = []
# for i in range(1, num + 1):
#     list.append(product(i))

# print(f"Произведения чисел от 1 до {num}:  {list}")


# Задача 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# n = int(input('Введите количество чисел в последовательности: ')) 

# def list (n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(list(n))
# print(round(sum(list(n))))



# Задача 4 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input("Введите число N:"))

from random import randint 
list1 = [randint(-N,N) for x in range(N)]
print(f"Заданный список = {list1}")

with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('2\n') 
    data.write('4\n')     #Добавление необходимых позиций 


def readfile():
    with open ("file.txt") as data:
        index = list (map(int, data.readlines()))
        print(f"Значения из файла={index}")
        return index

f = readfile()
product = 1
for i in range (len(f)):
    product *= list1 [f[i]]

print(f"Произведение элементов списка = {product}")

# Задача 5 Реализуйте алгоритм перемешивания списка.

