class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayAll()

    def displayAll(self):
        print "Price: " + str(self.price)
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        print "Tax: " + str(self.tax)

car1 = Car(2000, "35mph", "Full", "15mpg")
print ""
car2 = Car(2000, "5mph", "Not Full", "105mpg")
print ""
car3 = Car(15000, "75mph", "Full", "20mpg")
