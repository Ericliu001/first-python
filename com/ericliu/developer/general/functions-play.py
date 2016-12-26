def playRange(n = 10):
    for i in range(n):
        print(i, end=" ")
    print()


def call():
    playRange()
    playRange(12)
    playRange(5)


call()