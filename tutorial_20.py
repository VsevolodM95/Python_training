#tutorial #20 Creating functions

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read();
   
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()
   
current_file = open(input_file)

print "Printing the whole file:\n"

print_all(current_file)

print "Rewinding:\n"

rewind(current_file)

print "Printing some first lines: "

current_line = 1

print_a_line(current_line, current_file)

current_line = current_line +1

print_a_line(current_line, current_file)

current_line = current_line +1

print_a_line(current_line, current_file)
