total_1 = 0
total_2 = 0
for i in range(1,5):
    num = int(input('enter a number '))
    if num %2 == 0:
        total_1 = total_1 + num
    if num %2 != 0:
        total_2 = total_2 + num
print ('the odd numbers added = ',total_2)
print ('the even numbers added = ',total_1)