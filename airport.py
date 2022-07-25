'''airport'''
def addtime(h_old, m_old, h_new, m_new):
    '''add'''
    h_change = h_new +h_old
    m_change = m_new + m_old
    count_m = m_change//60
    m_change = m_change%60
    h_change = (h_change+ count_m)%24
    return (h_change, m_change)
 
def change(var_h, var_m, text):
    '''change'''
    count_m = var_m//60
    change_m = var_m%60
    count_h = (var_h+count_m)//12
    if (var_h+count_m)%12 == 0:
        change_h = 12
    else:
        change_h = (var_h+count_m)%12
    if count_h > 0:
        for var in range(count_h):
            if text == 'AM':
                text = 'PM'
            elif text == 'PM':
                text = "AM"
    return (change_m, change_h, text)
 
def plan(airport):
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
    airportend = input()
    timeex = input()
    htimeex = timeex[0:2]
    mtimeex = timeex[3:5]
    texttimeex = timeex[6:].upper()
    wheresym1 = airportend.index('(')
    wheresym2 = airportend.index(')')
    (hour, vminutes) = plan(airportend[wheresym1+1:wheresym2].upper())
    (h_change, m_change) = addtime(int(htimeex), int(mtimeex), hour, vminutes)
    (change_m, change_h, text) = change(h_change, m_change, texttimeex)
    print('BKK - %s'%(airportend[wheresym1+1:wheresym2]))
    print('%.02d:%.02d %s'%(change_h, change_m, text))
main()