a=int(input('Введите ваш возраст: '))
if a>120 or a==0:
    print('Ошибка, Вы еще не родились или уже мертвы')
elif a>10 and a<15:
    print('Вам',a,'лет')
else:
    i=a%10
    if i==1:
        print('Вам',a,'год')
    elif i>=2 and i<=4:
        print('Вам',a,'года')
    else:
        print('Вам',a,'лет')
