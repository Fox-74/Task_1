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
nn = 0
#i = -1 #Индикатор количества действий
#while True:
#    Nom_1 = list(input('Введите мат. операцию (+, -, *, **, /, //, %) и число: '))
#    i+=1
#    if Nom_1[0] != '=':
#        s.append(Nom_1)
#    else:
#        print(i)
#        print(s) #Проверка ввода.
#        print(s[0],s[1][0])
#        break
#_____________________________________________________
try:
    while nn != '=':
        nn = input('Введите операцию и число или = для вывода результата: ')
        if nn.startswith('+'):
            s = nn.replace('+','')
            nn = float(s)
            while True:
                nu = input('Введите операцию и число или = для вывода результата1: ')
                if nu.startswith('*'):
                    s = nu.replace('*', '')
                    nu = float(s)
                    nn *= nu
                elif nu.startswith('/'):
                    s = nu.replace('/', '')
                    nu = float(s)
                    nn /= nu
                elif nu == '=':
                    n += nn
                    print(f'Результат: {n}')
                    print(s)
                    nn = nu
                    break
 #           n += nn
        elif nn.startswith('-'):
            s = nn.replace('-','')
            nn = float(s)
            while True:
                nu = input('Введите операцию и число или = для вывода результата1: ')
                if nu.startswith('*'):
                    s = nu.replace('*', '')
                    nu = float(s)
                    nn *= nu
                elif nu.startswith('/'):
                    s = nu.replace('/', '')
                    nu = float(s)
                    nn /= nu
                elif nu == '=':
                    n -= nn
                    print(f'Результат: {n}')
                    print(s)
                    nn = nu
                    break
#            n -= nn
        elif nn.startswith('*'):
            s = nn.replace('*','')
            nn = float(s)
            n *= nn
        elif nn.startswith('/'):
            s = nn.replace('/', '')
            nn = float(s)
            n /= nn
 #       elif '**' in nn == True:
 #           n = list(nn)
 #           n **= float(nn[1])
        elif nn == '=':
            print(f'Результат: {n}')
            print(s)
            break
#       elif (nn[0]=='/' or nn[0]=='//' or nn[0]=='%') and nn[1]=='0':
#          print ('Ошибка! На ноль делить нельзя!')
#        elif nn[0]=='/':
#            n1/=float(nn[1])
#        elif nn[0]=='//':
#            n1//=float(nn[1])
#        elif nn[0]=='%':
#            n1%=float(nn[1])
        else:
            print ('Ошибка ввода!')
except ValueError:
    print ('Введи число и мат. операцию')