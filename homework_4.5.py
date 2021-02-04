# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def my_list(a, i):
    return a*i

new_list = {el for el in range (100,1001,2)}
print(reduce(my_list, new_list))

# -------



# def my_func(o)
# my_list = {el for el in range (100,1001,2)}
# print(sum(my_list))