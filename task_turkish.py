print("НАКОНЕЦ ТО!!!")
l=[]
calc=0
import random
while int(calc)<20:
    l.append(calc)
    calc=int(calc)+1
    random.shuffle(l)
print(l)

def minmax1 (x): 
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    return (minimum,maximum)
print(minmax1(l))

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]
print(l)




