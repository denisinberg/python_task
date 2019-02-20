month=int(input('Введите номер месяца: '))
if 0<month<=3:
    print('Зима')
elif 3<month<=6:
    print('Весна')
elif 6<month<=9:
    print('Лето')
elif 9<month<=12:
    print('Осень')
else:
    print('Неверный номер месяца')
