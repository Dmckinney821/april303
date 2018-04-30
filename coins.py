x = 0

while x < 5:
    y = input('Do you want another: '  )
    if y == 'yes':
        print('You have %d coin' % x)
        x = x + 1
    else:
        print('Bye')
    