#Калькулятор
#Проверка ввода
#while True:
#   try:
#       c = int(input("Введите число:"))
#        break
#    except ValueError:
#        print("Вы ввели не число! Попробуйте снова:")
#-----------------------------------------------------
#try:
#========================================================
#Ввод данных:
n = float(input('Введите число: '))
s = [] #Место хранения выражения
i = -1 #Индикатор количества действий
while True:
    Nom_1 = list(input('Введите мат. операцию (+, -, *, **, /, //, %) и число: '))
    i+=1
    if Nom_1[0] != '=':
        s.append(Nom_1)
    else:
        print(i)
        print(s) #Проверка ввода.
        print(s[0],s[1][0])
        break

#    while True:
#        nn = input('Введите операцию и число через пробел или = для вывода результата: ')
#        if '+' in nn == True:
#            n = list(nn)
#            n += float(nn[1])
#        elif '-' in nn == True:
#            n = list(nn)
#            n -= float(nn[1])
#        elif '*' in nn == True:
#            n = list(nn)
#            n *= float(nn[1])
#        elif '**' in nn == True:
#            n = list(nn)
#            n **= float(nn[1])
#       elif nn == '=':
#            print(f'Результат: {n}')
#            break
#        elif (nn[0]=='/' or nn[0]=='//' or nn[0]=='%') and nn[1]=='0':
#           print ('Ошибка! На ноль делить нельзя!')
#        elif nn[0]=='/':
#            n1/=float(nn[1])
#        elif nn[0]=='//':
#            n1//=float(nn[1])
#        elif nn[0]=='%':
#            n1%=float(nn[1])
#        else:
#            print ('Ошибка ввода!')
#except ValueError:
#    print ('Введи число и мат. операцию')