'''time'''
from datetime import datetime
from datetime import timedelta
def plan(airport):
    '''plan'''
    if airport == 'SYD':
        hour = 12
        minutes = 0
    elif airport == 'SGN':
        hour = 1
        minutes = 50
    elif airport == 'ATL':
        hour = 9
        minutes = 55
    elif airport == 'YVR':
        hour = 2
        minutes = 20
    elif airport == 'KTM':
        hour = 11
        minutes = 45
    return (hour, minutes)

def main():
    '''main'''
    fromairport = input()
    fromairport = fromairport
    airportend = input()
    timeex = input()
    htimeex = timeex[0:2]
    mtimeex = timeex[3:5]
    texttimeex = timeex[6:].upper()
    wheresym1 = airportend.index('(')
    wheresym2 = airportend.index(')')
    var_t = htimeex + ':'+ mtimeex +' ' + texttimeex.upper()
    vartx = datetime.strptime(var_t, '%I:%M %p')
    (vara, varb) = plan(airportend[wheresym1+1:wheresym2].upper())
    if vara >= 1440:
        vara = vara % 1440
    if varb >= 86400:
        varb = varb % 86400
    time_change = timedelta(hours=vara, minutes=varb)
    var3 = vartx + time_change
    var3 = var3.strftime('%I:%M %p')
    print('BKK - %s'%(airportend[wheresym1+1:wheresym2]))
    var3 = var3[:-2]+var3[-2:].upper()
    print(var3)
main()
