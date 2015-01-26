class Parent(object):
    def __init__(self):
        pass
    def printText(self):
        print "I'm papa"

class Child(Parent):
    def printText(self):
        super(Child, self).printText()
        print "I'm child"

c = Child()
print c.printText()