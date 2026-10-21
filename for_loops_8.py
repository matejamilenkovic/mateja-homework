total = 0
for i in range (5):
    num = int(input('enter a number '))
    q = input ('would you like this number to ba added? ')
    if q == 'yes':
        total = total + num
    if q == 'no':
        total = total
print('total = ',total)