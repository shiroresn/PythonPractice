class Parent:
    parentAttr = 100
    def __init__(self):
        print("calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("In Child Constructor")

    def childMethod(self):
        print("Calling child method")

c = Child()
c.setAttr(533)
c.getAttr()