# 4. По номеру месяца напечатать пору года
try:
    month = int(input('Enter the month:\n'))
    if month > 0:
        if month < 13:
            if month == 12 or month == 1 or month == 2:
                print('Month', month, 'is Winter.')
            elif 3 <= month <= 5:
                print('Month', month, 'is Spring.')
            elif 6 <= month <= 8:
                print('Month', month, 'is Summer.')
            else:
                print('Month', month, 'is Autumn.')
        else:
            print('There is no month the number of which is ' + str(month))
    else:
        print('There is no negative month.')
except ValueError:
    print('You entered the wrong data type. Please enter a number!')
