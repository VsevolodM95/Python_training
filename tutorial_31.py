#tutorial 31: making decisions, branching

print "Please, enter the number: "

num = raw_input(">")

if num > 0:
    print "Number is greater than zero"
elif num < 0:
    print "Number is lesser than zero"
else:
    print "Your number is zero!"
    
print "Please, enter some other number:"

num2 = raw_input(">")

a = num2 % [2]

if a == 0:
    print "Number can be divided on 2"
else:
    print "Number can't be divided on 2"
