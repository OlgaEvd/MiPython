#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
#¬ = знак "-" или not
# ⋁ = or
# ⋀ = and
#Вариант1
# x = input ("X:")
# y = input ("Y: ")
# z = input ("Z: ")
# num1 = not (x or y or z)
# num2 = not x and not y and not z
# if num1 == num2:
#         print (True)
# else:
#      print (False)


# if num1 > 0 and num2 > 0 or num1 < 0 and num2 < 0:
#     print (True)
# else:
#     print (False)

#Вариант2
def func(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (func(0, 0, 0) and func(0, 0, 1) and func(0, 1, 0) and 
func(0, 1, 1) and func(1, 0, 0) and func(1, 0, 1) and
func(1, 1, 0) and func(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")