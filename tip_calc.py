total = float(input('Total Bill Amount?'))
service = input('Level of Service?')
split = float(input('Split how many ways'))

if service == 'good':
    tip = total * 0.2
    total = tip + total
    split = total / split
    print('Tip amount? %.2f' % tip)
    print('Total amount? %.2f' % total)
    print('Amount per person: %.2f' %split)


elif service == 'fair':
    tip = total * 0.15
    total = tip + total
    split = total / split
    print('Tip amount? %.2f' %tip)
    print('Total amount? %.2f'  %total)
    print('Amount per person: %.2f'  %split)


elif service == 'bad':
    tip = total * 0.1
    total = tip + total
    split = total / split
    print('Tip amount? %.2f'  %tip)
    print('Total amount? %.2f'  %total)
    print('Amount per person: %.2f' %split)

else: 
    print("Do something")