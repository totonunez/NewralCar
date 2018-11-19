from random import choice, random
list=list()
x=0
while x<10:
    list.append(x)
    x += 1

y=0
while y<10:
    print((choice(list)))
    y +=1