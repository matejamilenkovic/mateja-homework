age = int(input('enter your age: '))
if age < 12:
    print('ur fare is 2 euros')
elif age > 65:
    travel = input('do you have a travel card?')
    if travel == 'yes':
        print('you go free')
    else:
        print('3 euros')
else:
    print('5 euros')