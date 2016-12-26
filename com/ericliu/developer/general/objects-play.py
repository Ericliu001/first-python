class Color():
    def __init__(self, shade):
        self.shade = shade

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.shade == other.shade

    def __hash__(self):
        return hash(self.shade)


a = Color(12)
b = Color(12)

print("a == b, {}".format(a == b))

name = "a" + " b" + str(a.shade)


def swapColors(a: Color):
    a = Color(24)
    print("The id of a is ", id(a))


print("The id of a is ", id(a))
swapColors(a)
print("The id of a is ", id(a))


