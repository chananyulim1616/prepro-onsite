'''drop'''
def main():
    '''main'''
    grade1 = float(input())
    if grade1 < 1:
        print("I'm so sad.")
    elif grade1 < 2:
        grade2 = (4 - grade1)
        print('%.2f'%grade2)
    else:
        print("I'm so happy.")
main()
