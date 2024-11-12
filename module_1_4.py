#Практическая работа по уроку "Организация программ и методы строк"
my_string = input("ФИО: ")
print(my_string)
total = 0
for i in range(len(my_string)):
    total = total + 1
print("Количество символов:",total)
print("Верхний регистр:",my_string.upper()  )
print("Нижний регистр:",my_string.lower() )
print("Удаляем пробелы:",my_string.replace(" ",""))
print("Выводим первый введенный симфол:",my_string[0])
print("Выводим последний введенный симфол:",my_string[-1])
