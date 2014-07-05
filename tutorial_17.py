#tutorial #17

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Now we are gonna to copy file %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." %len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready. Hit ENTER to continue or CTRL+C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Done!"

out_file.close()
in_file.close()
