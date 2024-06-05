##Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##Dog is-a Animal.
class Dog(Animal):

    def __init__(self, name):
        ##
        self.name=name

##Cat is-a Animal.
class Cat(Animal):

    def __init__(self, name):
        
        self.name=name

##Person is-a object.
class Person(object):

    def __init__(self,name):

        self.name=name

        ##person has-a pet of some kind.
        self.pet=None

##Employee is-a person.
class Employee(Person):

    def __init__(self, name, salary):
        ##?? hmm what is is this strange magic.
        super(Employee, self).__init__(name)

        self.salary=salary

##Fish is-a object.
class Fish(object):
    pass

##Salmon is-a Fish.
class Salmon(Fish):
    pass

##Halibut is-a Fish.
class Halibut(Fish):
    pass


##rover is-a Dog.
rover=Dog("Rover")

##Satan is -a Cat.
satan=Cat("Satan")

##Mary is-a Person.
mary=Person("Mary")

##From mary , get the pet attribute and set it to Satan.
mary.pet=satan

##set Frank to an instance of class Employee.
frank=Employee("Frank",120000)

##From Frank , get the pet attribute and set it to rover.
frank.pet=rover

##set flipper to an instance of class Fish.
flipper=Fish()

##set crose to an instance of class Salmon.
crouse=Salmon()

##set harry to an instance of class Halibut.
harry=Halibut()