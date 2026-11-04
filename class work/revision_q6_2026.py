secret = 3
num = int (input('guess a number between 1 and 10 '))
if num == 3 :
    print ('bingo')
if num + 1 == 3:
    print ('close enough')
elif num != 3:
    print ('incorrect')