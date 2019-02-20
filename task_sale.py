print('Вы в магазине. Вам нужно купить хлеб, молоко и масло')
print('Хлеб стоит 4 грн., молоко 10 грн., а масло 20 грн.')
cash = int(input('Сколько у Вас денег?'))
bread = 4
milk = 10
butter = 20
a = bread + milk + butter
if a < cash :
    print('стоимость товаров ' + str(a) + ' грн.')
    b = cash - a
    print('Отлично! Ваша сдача ' + str(b) + ' грн.')
elif a == cash :
    print('Спасибо, что без сдачи!')
else :
    print('Сумма недостаточна')
