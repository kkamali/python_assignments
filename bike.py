class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price: " + str(self.price) + ", Max Speed: " + self.max_speed + ", Total Miles: " + str(self.miles)

    def ride(self):
        print "Riding..."
        self.miles = self.miles + 10
        return self

    def reverse(self):
        print "Reversing..."
        if (self.miles - 5 > 0):
            self.miles = self.miles - 5
        else:
            self.miles = 0
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "30mph")
bike3 = Bike(350, "35mph")

bike1.ride().ride().ride().ride().reverse().displayInfo()
print ""

bike2.ride().ride().reverse().reverse().displayInfo()
print ""

bike3.reverse().reverse().reverse().displayInfo()
