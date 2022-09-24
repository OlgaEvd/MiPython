#Метод № 1: алгоритм перетасовки Фишера–Йейтса

 
import random
 
test_list = [1, 4, 5, 6, 3]
print ("Исходный список: " + str(test_list))
 
# алгоритм перетасовки Фишера–Йейтса
for i in range(len(test_list)-1, 0, -1):
       
    j = random.randint(0, i + 1)
      
    test_list[i], test_list[j] = test_list[j], test_list[i]
     
print ("Перемешанный список : " +  str(test_list))