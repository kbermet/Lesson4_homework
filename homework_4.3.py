# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

# my_list =[]
new_list = {el for el in range(20, 241, 20)}

print(new_list)