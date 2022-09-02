#Вариант1
# num = [int (i) for i in input ("Введите целые числа через пробел: ").split ()[:5]]
# print ("МАКСИМУМ:", max (num))

#Вариант2

print(max([int (i) for i in input ("Введите целые числа через пробел: ").split ()[:5]]))


#Вариант 3
# num = [int (i) for i in input ().split ()[:5]]
# max_num = num [0]
# for i in range (len(num)):
#     if num[i] > max_num:
#        max_num = num [i]
# print (num)
# print (max_num)