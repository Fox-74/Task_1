#Проверка числа на простоту
#Первая версия проверки ввода:
#while True:
#    a = input("Введите число: ")
#    if not a.isnumeric():
#        print("Вы ввели не число! Попробуйте снова: ")
#    else:
#        print("OK")
#        break
#--------------------------------------------------------
#  (0_0)
#Вторая версия проверки ввода:
while True:
    try:
        c = int(input("Введите число:"))
        break
    except ValueError:
        print("Вы ввели не число! Попробуйте снова:")
#-----------------------------------------------------
#Тело проверки простоты числа
k = 1
if c % 2 == 0:
    if c == 2:
        k = 0
        print("Ok")
    else:
        n = 3
        print(c)
        while n * n <= c and c % n != 0:
            n += 2
            if n * n > c:
                k = 0
                print("OK")
            else:
                k = 1
                print("NO")
if k == 1:
    print("OK!")
else:
    print("NO!!!")