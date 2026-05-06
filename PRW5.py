color = input('enter a color of an item: ')
if color == 'red':
    fruit = input('is it a fruit?')
    if fruit == 'yes':
        print('it could be a tomato or apple...')
    else:
        print('it could be a rose...')
elif color == 'yellow':
    fruit = input('is it a fruit?')
    if fruit == 'yes':
        print(' it could be a banana...')
    else:
        print('is it corn or a mrigold?')
else:
    print('i cant help.')
    