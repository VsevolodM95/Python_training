#tutorial #16

from sys import argv

script, filename = argv

print "I'm gonna erase file %r" % filename
print "Hit CTRL+C to cancel erasing"
print "Or ENTER to apply it."

raw_input("?");

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file!\n"
target.truncate()

print "Please, enter new content for the file:"

line_1 = raw_input("Enter line #1:")
line_2 = raw_input("Enter line #2:")
line_3 = raw_input("Enter line #3:")

print "They will be placed in the file."

target.write(line_1+"\n"+line_2+"\n"+line_3+"\n")

print "Finish!"

target.close()
