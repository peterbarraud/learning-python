def usingFormat():
    # using positional args
    print('{} and {} went up the hill'.format('Jack', 'Jill'))
    # using numbered args
    print('{1} and {0} went up the hill'.format('Jill', 'Jack'))
    # using named args
    print('{jack} and {jill} went up the hill'.format(jill='Jill', jack='Jack'))

    # makes concatenating string and numbers easier than something like (which needs lots of casting):
    # print(1 + ' day...')
    print('{one} day {jack} and {jill} went up the hill'.format(one=1, jack='Jack', jill='Jill'))

def usingjoin():
    s1 = 'string 1'
    s2 = 'string 2'
    print(' '.join([s1, s2]))

def slicing_and_dicing():
    s = 'abcdefghijklmnopqrstuvwxyz'
    # start at 0 and do 2
    print(s[0:2])
    # start at 0 and do all but 2
    print(s[0:-2])
    # start at 5 and to the end
    print(s[5:])
    # start at 5 from the end and to the end
    print(s[-5:])
    # start at 2 go to 8 skipping 2 at a time
    print(s[2:8:2])

if __name__ == "__main__":
    usingFormat()
