height = int(input('Height'))
width = int(input('Width'))

something = ""
better = ""

column = 1
while column <= width:
    something= something + '*'
    column = column + 1

column = 1
while column <= width:
    if column == 1 or column == width:
        better = better + '*'
    else:
        better = better + ' ' 
    column = column + 1


row = 1
while row <= height:
    if row == 1 or row == height:
        print(something)
    else:
        print(better)
    row = row + 1

