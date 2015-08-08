__author__ = 'nata'
prop1 = "Hello Stan"
class Myclass():
    # default property
    prop1 ="I am a class property!"
    # method which sets a new property
    def setProperty(self, newval):
        self.prop1 = newval
        # method which return the property
    def getProperty(self):
        return self.prop1

    def getTrueProperty(self):
        return prop1

obj = Myclass()
print (obj.prop1)
obj.setProperty('Hello Nata')
print (obj.getProperty())
print(obj.getTrueProperty())
# obj1 = Myclass()
# print (obj1.getProperty())



