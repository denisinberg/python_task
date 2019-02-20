m=int(input('Твой возраст: '))
k=m%10
if (m>9)and(m<20)or(m>110)or(k>4)or(k==0):
    print('Вам',m,'лет')
else:
    if k==1:
        print('Вам',m,'год')
    else:
        print('Вам',m,'года')
