immutable_var = 1, 2, "bin", "max"                      # Создаем переменную, присваемаем кортеж
print(immutable_var)                                    # Выводим кортеж
immutable_var[1] = 20                                   # Изменяем кортеж и получаем ошибку, так как данные не могу быть изменены
print(immutable_var)                                    # пытаемся вывести 
mutable_list = [1, 2, "max1", "max2", "max3"]           # Создаем изменяемую структуру
mutable_list[3] = "max10"                               # Изменяем max2
print(mutable_list)                                     # Выводим

