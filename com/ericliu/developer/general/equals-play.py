def swap(a, b):
    print("parameter a address in swap function {}".format(id(a)))
    a, b = b, a
    print("parameter a address in swap function {}".format(id(a)))
    print("a={}, b={} in the swap function.".format(a, b))


a = 0
b = 1
print("Address of a is {}".format(id(a)))
swap(a ,b)
print("a={}, b={} after swap is called".format(a, b))
print(type(b))

class Haha():
    x = 1;

ha = Haha();
print("x={}".format(ha.x))

def changeX(haha):
    haha.x = 10


changeX(ha)
print("x={}".format(ha.x))
print(id(ha))
print(type(ha))

