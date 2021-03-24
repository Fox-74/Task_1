#Калькулятор
#========================================================
#Ввод данных и обработка данных
while True:
    try:
        n = float(input('Введите число: '))
        break
    except ValueError:
        print('Ошибка ввода! TrueВы ввели не число!')
s = [] #Место хранения
nn = 0
nu = 0
ns = 0
#_____________________________________________________
try:
    while nn != '=':
#Первый контур вычислений
        nn = input('Введите операцию и число или = для вывода результата: ')
        if nn.startswith('+'):
            s = nn.replace('+','')
            nn = float(s)
            while nu != '=':
#Второй контур вычислений
                nu = input('Введите операцию и число или = для вывода результата: ')
                if nu.startswith('**'):
                    s = nu.replace('**','')
                    nu = float(s)
                    nn **= nu
                elif nu.startswith('*'):
                    s = nu.replace('*','')
                    nu = float(s)
                    while True:
                        # Третий контур вычислений
                        ns = input('Введите операцию и число или = для вывода результата: ')
                        if ns.startswith('**'):
                            s = ns.replace('**', '')
                            ns = float(s)
                            nu **= ns
                        elif ns.startswith('*'):
                            s = ns.replace('*', '')
                            ns = float(s)
                            nn *= nu
                            nn *= ns
                        elif ns.startswith('//'):
                            s = ns.replace('//', '')
                            ns = float(s)
                            nu //= ns
                        elif ns.startswith('/'):
                            s = ns.replace('/', '')
                            ns = float(s)
                            nn *= nu
                            nn /= ns
                        elif ns.startswith('+'):
                            s = ns.replace('+', '')
                            ns = float(s)
                            nn *= nu
                            n += nn
                            n += ns
                        elif ns.startswith('-'):
                            s = ns.replace('-', '')
                            ns = float(s)
                            nn *= nu
                            n += nn
                            n -= ns
                        elif ns == '=':
                            nn *= nu
                            n += nn
                            print(f'Результат: {n}')
                            nu = ns
                            nn = nu
                            break
                elif nu.startswith('//'):
                    s = nu.replace('//', '')
                    nu = float(s)
                    nn //= nu
                elif nu.startswith('/'):
                    s = nu.replace('/', '')
                    nu = float(s)
                    while True:
                        # Третий контур вычислений
                        ns = input('Введите операцию и число или = для вывода результата: ')
                        if ns.startswith('**'):
                            s = ns.replace('**', '')
                            ns = float(s)
                            nu **= ns
                        elif ns.startswith('*'):
                            s = ns.replace('*', '')
                            ns = float(s)
                            nn /= nu
                            nn *= ns
                        elif ns.startswith('//'):
                            s = ns.replace('//', '')
                            ns = float(s)
                            nu //= ns
                        elif ns.startswith('/'):
                            s = ns.replace('/', '')
                            ns = float(s)
                            nn /= nu
                            nn /= ns
                        elif ns.startswith('+'):
                            s = ns.replace('+', '')
                            ns = float(s)
                            nn /= nu
                            n += nn
                            n += ns
                        elif ns.startswith('-'):
                            s = ns.replace('-', '')
                            ns = float(s)
                            nn /= nu
                            n += nn
                            n -= ns
                        elif ns == '=':
                            nn *= nu
                            n += nn
                            print(f'Результат: {n}')
                            nu = ns
                            nn = nu
                            break
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
                    nn = nu
                    break
        elif nn.startswith('-'):
            s = nn.replace('-','')
            nn = float(s)
            while nu != '=':
#Второй контур вычислений
                nu = input('Введите операцию и число или = для вывода результата1: ')
                if nu.startswith('**'):
                    s = nu.replace('**','')
                    nu = float(s)
                    nn **= nu
                elif nu.startswith('*'):
                    s = nu.replace('*','')
                    nu = float(s)
                    while True:
                        # Третий контур вычислений
                        ns = input('Введите операцию и число или = для вывода результата: ')
                        if ns.startswith('**'):
                            s = ns.replace('**', '')
                            ns = float(s)
                            nu **= ns
                        elif ns.startswith('*'):
                            s = ns.replace('*', '')
                            ns = float(s)
                            nn *= nu
                            nn *= ns
                        elif ns.startswith('//'):
                            s = ns.replace('//', '')
                            ns = float(s)
                            nu //= ns
                        elif ns.startswith('/'):
                            s = ns.replace('/', '')
                            ns = float(s)
                            nn *= nu
                            nn /= ns
                        elif ns.startswith('+'):
                            s = ns.replace('+', '')
                            ns = float(s)
                            nn *= nu
                            n -= nn
                            n += ns
                        elif ns.startswith('-'):
                            s = ns.replace('-', '')
                            ns = float(s)
                            nn *= nu
                            n -= nn
                            n -= ns
                        elif ns == '=':
                            nn *= nu
                            n -= nn
                            print(f'Результат: {n}')
                            nu = ns
                            nn = nu
                            break
                elif nu.startswith('//'):
                    s = nu.replace('//','')
                    nu = float(s)
                    nn //= nu
                elif nu.startswith('/'):
                    s = nu.replace('/','')
                    nu = float(s)
                    while True:
                        # Третий контур вычислений
                        ns = input('Введите операцию и число или = для вывода результата: ')
                        if ns.startswith('**'):
                            s = ns.replace('**', '')
                            ns = float(s)
                            nu **= ns
                        elif ns.startswith('*'):
                            s = ns.replace('*', '')
                            ns = float(s)
                            nn /= nu
                            nn *= ns
                        elif ns.startswith('//'):
                            s = ns.replace('//', '')
                            ns = float(s)
                            nu //= ns
                        elif ns.startswith('/'):
                            s = ns.replace('/', '')
                            ns = float(s)
                            nn /= nu
                            nn /= ns
                        elif ns.startswith('+'):
                            s = ns.replace('+', '')
                            ns = float(s)
                            nn /= nu
                            n -= nn
                            n += ns
                        elif ns.startswith('-'):
                            s = ns.replace('-', '')
                            ns = float(s)
                            nn /= nu
                            n -= nn
                            n -= ns
                        elif ns == '=':
                            nn *= nu
                            n -= nn
                            print(f'Результат: {n}')
                            nu = ns
                            nn = nu
                            break
                elif nu.startswith('+'):
                    s = nu.replace('+','')
                    nu = float(s)
                    n += nn
                    n += nu
                elif nu.startswith('-'):
                    s = nu.replace('-','')
                    nu = float(s)
                    n += nn
                    n -= nu
                elif nu == '=':
                    n -= nn
                    print(f'Результат: {n}')
                    nn = nu
                    break
        elif nn.startswith('**'):
            s = nn.replace('**','')
            nn = float(s)
            n **= nn
        elif nn.startswith('*'):
            s = nn.replace('*','')
            nn = float(s)
            while True:
                # Второй контур вычислений
                ns = input('Введите операцию и число или = для вывода результата: ')
                if ns.startswith('**'):
                    s = ns.replace('**', '')
                    ns = float(s)
                    nn **= ns
                elif ns.startswith('*'):
                    s = ns.replace('*', '')
                    ns = float(s)
                    n *= nn
                    n *= ns
                elif ns.startswith('//'):
                    s = ns.replace('//', '')
                    ns = float(s)
                    nn //= ns
                elif ns.startswith('/'):
                    s = ns.replace('/', '')
                    ns = float(s)
                    n *= nn
                    n /= ns
                elif ns.startswith('+'):
                    s = ns.replace('+', '')
                    ns = float(s)
                    n *= nn
                    n += ns
                elif ns.startswith('-'):
                    s = ns.replace('-', '')
                    ns = float(s)
                    n *= nn
                    n -= ns
                elif ns == '=':
                    n *= nn
                    print(f'Результат: {n}')
                    nn = ns
                    break
        elif nn.startswith('//'):
            s = nn.replace('//','')
            nn = float(s)
            n //= nn
        elif nn.startswith('/'):
            s = nn.replace('/','')
            nn = float(s)
            while True:
                # Второй контур вычислений
                ns = input('Введите операцию и число или = для вывода результата: ')
                if ns.startswith('**'):
                    s = ns.replace('**', '')
                    ns = float(s)
                    nn **= ns
                elif ns.startswith('*'):
                    s = ns.replace('*', '')
                    ns = float(s)
                    n *= nn
                    n /= ns
                elif ns.startswith('//'):
                    s = ns.replace('//', '')
                    ns = float(s)
                    nn //= ns
                elif ns.startswith('/'):
                    s = ns.replace('/', '')
                    ns = float(s)
                    n /= nn
                    n /= ns
                elif ns.startswith('+'):
                    s = ns.replace('+', '')
                    ns = float(s)
                    n /= nn
                    n += ns
                elif ns.startswith('-'):
                    s = ns.replace('-', '')
                    ns = float(s)
                    n /= nn
                    n -= ns
                elif ns == '=':
                    n /= nn
                    print(f'Результат: {n}')
                    nn = ns
                    break
            #n /= nn
        elif nn == '=':
            print(f'Результат: {n}')
            break
        else:
            print ('Ошибка ввода! Попробуйте еще раз!')
except ValueError:
    print('Вы ввели неверное выражение')