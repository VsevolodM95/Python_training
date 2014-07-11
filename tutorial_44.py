#tutorial 44

class Parent(object): #Creating class Parent

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"
#creating three functions of class Parent
class Child(Parent): # creating class Child is-a Parent

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()#creating object dad class Parent
son = Child()#creating object son class Child

dad.implicit() #call Parent function
son.implicit() # as long as Son doesn't have the function with the same name, call Parent function

dad.override() # call parent function
son.override() # son has its own function with that name so we call it instead of Parent

dad.altered() # call parent function
son.altered() # with the help of Super we get the Parents version of this function and the sons version 
