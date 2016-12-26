class Animal():
    # actions = dict(
    #     eat = "An animal is eating something."
    #     , run = "An animal is running."
    # )

    def eat(self):
        return self.actions['eat']

    def run(self):
        return self.actions['run']



class Dog(Animal):
    actions = dict(
        eat = "The dog is eating bones."
        , run = "The dog is running after a rabbit."
    )


luis = Dog()
print(luis.eat())

animal = Animal()
animal.eat()