__author__ = 'nata'

class Encapsulation:
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        # using _ makes an object protected
        self.__private = c
        # using __ makes an object private

x = Encapsulation(11, 23, 17)
print x.public

x.public = 22
print x.public

class MyCar:
    def __init__(self, doors = None, color = None):
        if doors is None :
            doors = 2
        if color is None :
            color = "black"

        _wheels = 4

        print "Our car has %s doors" % (doors)
        print "Our car has %s color\n" % (color)


if __name__ == '__main__' :
    car1 = MyCar()
    car2 = MyCar(4, 'green')

class Myclass():
    # default property
    prop1 ="I am a class property!"
    # method which sets a new property
    def setProperty(self, newval):
        self.prop1 = newval
    # method which return the property
    def getProperty(self):
        return self.prop1

obj = Myclass()
print (obj.prop1)
obj.setProperty('I am a class property value!')
print (obj.getProperty())
obj1 = Myclass()
print (obj1.getProperty())