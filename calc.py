#Калькулятор
#Проверка ввода
#while True:
#   try:
#       c = int(input("Введите число:"))
#        break
#    except ValueError:
#        print("Вы ввели не число! Попробуйте снова:")
#========================================================
#Ввод данных:
n = float(input('Введите число: '))
s = [] #Место хранения выражения
nn = 0
#_____________________________________________________
try:
    while nn != '=':
        nn = input('Введите операцию и число или = для вывода результата: ')
        if nn.startswith('+'):
            s = nn.replace('+','')
            nn = float(s)
            while True:
                nu = input('Введите операцию и число или = для вывода результата: ')
                if nu.startswith('*'):
                    s = nu.replace('*', '')
                    nu = float(s)
                    nn *= nu
                elif nu.startswith('/'):
                    s = nu.replace('/', '')
                    nu = float(s)
                    nn /= nu
                elif nu.startswith('+'):
                    s = nu.replace('+', '')
                    nu = float(s)
                    n += nn
                    n += nu
                elif nu.startswith('-'):
                    s = nu.replace('-', '')
                    nu = float(s)
                    n += nn
                    n -= nu
                elif nu == '=':
                    n += nn
                    print(f'Результат: {n}')
                    print(s)
                    nn = nu
                    break
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
                elif nu.startswith('+'):
                    s = nu.replace('+', '')
                    nu = float(s)
                    n += nn
                    n += nu
                elif nu.startswith('-'):
                    s = nu.replace('-', '')
                    nu = float(s)
                    n += nn
                    n -= nu
                elif nu == '=':
                    n -= nn
                    print(f'Результат: {n}')
                    print(s)
                    nn = nu
                    break
        elif nn.startswith('*'):
            s = nn.replace('*','')
            nn = float(s)
            n *= nn
        elif nn.startswith('/'):
            s = nn.replace('/', '')
            nn = float(s)
            n /= nn
        elif nn == '=':
            print(f'Результат: {n}')
            print(s)
            break
        else:
            print ('Ошибка ввода!')
except ValueError:
    print ('Введи число и мат. операцию')