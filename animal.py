class Animal(object):
        def __init__(self, name):
            self.health = 100
            self.name = name

        def walk(self):
            self.health -= 1
            return self

        def run(self):
            self.health -= 5
            return self

        def displayHealth(self):
            print self.name + ", health = " + str(self.health)


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 10
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "this is a dragon!"
        super(Dragon, self).displayHealth()

animal = Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()

dog = Dog("doggo")
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("smauggie")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
