#tutorial 42
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal inherited class
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal inherited class
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

##Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Cat is-a Person inherited class
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a inherited Fish object
class Salmon(Fish):
    pass

## Halibut is-a inherited Fish object
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satar is-a Cat
satan = Cat("Satan")

## maru is-a person
mary = Person("Mary")

## marys pet is satan
mary.pet = satan

## Frank is-a employee which has-a name Frank and salary 120000
frank = Employee("Frank", 120000)

## franks pet is rober
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Hallibut
harry = Halibut()

