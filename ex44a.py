class Parent(object):   

    def implicit(self):
        print("PARENT implicit()")

    class Child(Parent):     #this class inherits the property of parent class.
        pass

dad = Parent()   #creating an instance of parent class.
son = Child()     #creating an instance of child class.

dad.implicit()    #accessing the method inside the class.
son.implicit()