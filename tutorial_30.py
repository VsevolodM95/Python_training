#tutorial 30: working with if statement

a = 10
b = 20
c = 30

if a>b:
    print "a>b"

elif a>c:
    print "a>c"

else:
    print "a - minimum"
    
if b + c == 50:
    print "%d + %d = 50" % (b, c)
else:
    print "%d + %d != 50" % (b, c)
