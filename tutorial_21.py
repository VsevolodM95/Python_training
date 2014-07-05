#tutorial #21 Functions can return something

def summing(a,b):
    print "a+b=", a+b
    return a+b
   
def substract(a,b):
    print "a-b=", a-b
    return a-b

def multiply(a,b):
    print "a*b=", a*b
    return a*b
    
def divide(a,b):
    print "a/b=", a/b
    return a/b
    
print "Lets test our functions!\n"

age = summing (20, 25)
height = substract(28, 4)
weight = multiply(90, 2)
iq = divide (200, 2)

print "Age = %d, height = %d, weight = %d, iq = %d\n" % (age, weight, height, iq)

# A PUZZLE!

res = summing(age, substract(height, multiply(weight, divide(iq,2))))

print "Res=", res
