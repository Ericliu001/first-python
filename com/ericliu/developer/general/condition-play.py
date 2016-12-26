def isGreater(a, b):
    str = "a is greater." if a > b else "a is not greater."
    print(str)


def compare(a, b):
    if a > b:
        print("a is greater than b")

    elif a < b:
        print("a is smaller than b")

    else:
        print("a equals b")


a, b = 1, 0

isGreater(a, b)
compare(a, b)
