# so lets say we take user input how can we let them know its invalid

num = input('Enter a integer number: ')
try:
    nummm = int(num)
    print('GOOD WORK')
except:
    nummm = 'INVALID'
    print(nummm)
