a=int(input('Введите возраст Андрея: '))
b=int(input('Введите возраст Борис: '))
c=int(input('Введите возраст Виктор: '))
if a>b and a>c:
    print('Андрей старше всех')
elif b>a and b>c:
    print('Борис старше всех')
elif b<c>a:
    print('Виктор старше всех')
elif a==b>c:
    print('Андрей и Борис старше Виктора')
elif a==c>b:
    print('Андрей и Виктор старше Бориса')
elif b==c>a:
    print('Борис и Виктор старше Андрея')
else:
    print('Андрей,Борис и Виктор одного возраста')

