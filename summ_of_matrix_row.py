from random import randint

a = []

r = int(input('Enter line of row: '))
c = int(input('Enter line of column: '))

for i in range(r):
    b = []
    for j in range(c):
        b.append(randint(0,100))
        #b.append(int(input('Enter a numbre: '))) # so you can input numbre's
    a.append(b) 


for i in a:
    print(i)  


for i in range(r):
    sum = 0
    for j in range(c):
        sum+=a[i][j]
    print('sum of ',i + 1,'row = ',sum)    
