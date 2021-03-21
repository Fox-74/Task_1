#Проверка числа на простоту
#  (0_0)
while True:
    try:
        с = int(input("Введите число:"))
        break
    except ValueError:
        print("Вы ввели не число! Попробуйте снова:")


print(isinstance(с,int))