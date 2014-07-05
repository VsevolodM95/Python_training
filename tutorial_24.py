#tutorial #24 More practice

print """
In this tutorial I should practice everything I've learned so far.
Using three double quotes I can type with no limits
"""

my_str = "String with \n escape-sequence \t \' \\ characters\\ \'"

print "-"*10 #I can use this for printing my character 10 times
print my_str
print "-"*11

six = (2*3+0-2+2)*1

print "Here i should get six %d" % six

def my_func(a, b, c):
    b = a+c
    a = b*c
    c = a+b+c
    return c

print "Some arythmetic: ", my_func (2,3,4)
