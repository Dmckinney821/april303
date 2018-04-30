x=int(input('Height: '))
y=int(input('Width: '))
while x > 0 :
    while y > 0:
        print('*' if x in(0,(2*n)+1) or y in(0,n+1) else ' ', end=' ')
    print()