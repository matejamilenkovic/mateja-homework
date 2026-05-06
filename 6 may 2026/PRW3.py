age = int(input('enter your age: '))
if age >= 18:
    adult = input('do you have a drivers license?')
    if adult == 'yes':
        print('you can rent a car')
    else:
        print('you cannot rent a car')
else:
    print('you cannot rent a car')