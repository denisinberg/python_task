print("НАКОНЕЦ ТО!!!")
import random 
l=[] 
for z in range(10):
    l.append(random.randint(0, 100))
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




