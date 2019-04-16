vvod = input('Enter name: ')

human = {'Turok':{'age':28,'height':'175cm','profession':'DevOps'},
         'Den'  :{'age':24,'height':'192cm','profession':'PyDev' }
         }

Turok = 'Turok'
turok = 'turok'
Den = 'Den'
den = 'den'

if vvod == Turok or turok:
    print(human['Turok'])

elif vvod == Den or den:
    print(human['Den'])



