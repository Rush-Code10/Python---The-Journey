# hohoho

day = input('Enter Day: ')
month = input('Enter Month: ')

try:
    dayy = int(day)
    monthh = int(month)
    if(monthh == 12):
       if(dayy>=25 or dayy<31):
           print('HOHO ITS CHRISTMAS YOUNG ONE')
       else:
           print('ITS A RANDOM DAY')
    elif(monthh == 1):
        if(dayy == 1):
            print('HAPPY NEW YEAR YOUNG ONE')
        else:
            print('ITS A RANDOM DAY')
    else:
        print('ITS A RANDOM MONTH YOUNG ONE')
except:
    print("INVALID")