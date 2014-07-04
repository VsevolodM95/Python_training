#tutorial #15
#READING FROM THE FIIILE!

from sys import argv

script, filename = argv

txt = open(filename) # much more easier than in other languages, Thanks!

print "Here's your file %r:" % filename
print txt.read() #one damn command instead of playing with looping

print "Type the filename again:"

file_again = raw_input("->")

txt_again = open(file_again)

print txt_again.read()
