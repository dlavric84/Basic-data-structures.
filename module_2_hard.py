#Задание "Слишком древний шифр":
pass_ = 0
while not int(pass_) in range(1, 20):
    pass_ = int(input('Введите число от 3 до 20: '))
    if pass_ > 20:
        print("Не допустимое значение: ")
        print("Введите число от 3 до 20: ")
        break
else:
    def get_passwd(number):
        paswd = ''
        for i in range(1, number):
            for j in range(2, number):
                if j <= i:
                    continue
                if number % (i + j) == 0:
                    paswd += str(i) + str(j)
        return paswd
    result = get_passwd(pass_)
    print('Пароль:', result)
