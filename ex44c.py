class Parent(object):   

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()   #redirecting to the function inside the base class.
        print("CHILD,AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()