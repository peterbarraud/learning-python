
def addingtwointegers():
    i = input('first num: ')
    j = input('second num: ')
    try:
        print(int(i) + int(j))
    except ValueError as ve:
        print(ve)

def addingtwonumbers():
    i = input('first num: ')
    j = input('second num: ')
    try:
        print(float(i) + float(j))
    except ValueError as ve:
        print(ve)

def addingtwostrings():
    i = input('first name: ')
    j = input('second name: ')
    print('Hi ' + i + ' ' + j)
    # that said, `string.format` is defintely a better choice here

if __name__ == "__main__":
    addingtwostrings()