#Метод № 1: алгоритм перетасовки Фишера–Йейтса

 
# import random
 
# test_list = [1, 4, 5, 6, 3]
# print ("Исходный список: " + str(test_list))
 
# # алгоритм перетасовки Фишера–Йейтса
# for i in range(len(test_list)-1, 0, -1):
       
#     j = random.randint(0, i + 1)
      
#     test_list[i], test_list[j] = test_list[j], test_list[i]
     
# print ("Перемешанный список : " +  str(test_list))

# Метод № 2: использование random.shuffle()
 
# import random
# test_list = [1, 2, 3, 4, 5]
# print ("The original list is : " + str(test_list))
# random.shuffle(test_list)
# print ("The shuffled list is : " +  str(test_list))



#Метод № 3: использование random.sample()
import random
test_list = [1, 2, 3, 4, 5]
print ("The original list is : " + str(test_list))
res = random.sample(test_list, len(test_list))
print ("The shuffled list is : " +  str(res))