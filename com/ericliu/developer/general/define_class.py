class Fibonacci():
    def __init__(self):
        self.a = 0
        self.b = 1

    def series(self):
        while True:
            yield self.b
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci()
for i in f.series():
    if i > 100: break
    print(i);
