#Подсчет гласных
#__________________________________________
s = {'a':0, 'e':0,'y':0,'u':0,'i':0,'o':0}
a = input('Введите текст: ').lower()
for i in a:
    if i in s.keys():
        s[f'{i}']+=1
for key, value in s.items():
  print("{0}: {1}".format(key,value), end='| '),