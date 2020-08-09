def lists():
    l = [1]
    l.append(2)
    print('\n'.join(l))

def dicts():
    d = {'a':1,'b':2}
    print(d['a'])
    if (d.get('a')):
        print(d['a'])

def main():
    dicts()


if __name__ == "__main__":
    main()