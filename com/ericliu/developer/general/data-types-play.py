def playInt():
    a = 42.3
    print(type(a), a)

    b = int(a)
    print(type(b), b)

    c = a / 3
    print(type(c), c)

    d = a // 3
    print(type(d), d)


playInt()


def playTuple():
    a = (1, 2, 3)
    print(type(a), a)


playTuple()


def playString():
    s = '''\
        ha
        ha
        ha,
        this
        is
        awesome
    '''
    for i in s:
        return i


playString()


def playCollections():
    t = (1, 2, 'a', 'b')
    for i in t:
        print(i)

    i = 0
    while i < len(t):
        i += 1

    l = [1, 2] + [3, 4]
    print(l)
    isInTheList = 5 in l
    print(isInTheList)

playCollections()
