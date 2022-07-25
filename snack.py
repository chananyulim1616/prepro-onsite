'''snack'''
def main():
    '''main'''
    money = int(input())
    money1 = money
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    stat = True
    if money - water >= 0 and stat == True:
        money = money - water
    else:
        stat = False
    psnack1 = (10 + ((money%3)*5))*snack1
    if money - psnack1 >= 0 and stat == True:
        money = money - psnack1
    else:
        stat = False
    psnack2 = (12 + ((money%3)*3))*snack2
    if money - psnack2 >= 0 and stat == True:
        money = money - psnack2
    else:
        stat = False
    psnack3 = (5 + ((money%3)*2))*snack3
    if money - psnack3 >= 0 and stat == True:
        money = money - psnack3
    else:
        stat = False
    if stat == True:
        print('Now you have %d left.'%money)
        print("Here's your order!")
        print('Water: %d baht'%water)
        print('Snack number 1: %d baht'%psnack1)
        print('Snack number 2: %d baht'%psnack2)
        print('Snack number 3: %d baht'%psnack3)
    else:
        print('Now you have %d left.'%money1)
        print("You don't have enough money!")
main()
