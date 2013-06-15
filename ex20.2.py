from sys import argv
script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

def print_where(f):
	print "current file position: %d\n" % f.tell()

current_file = open(input_file)

print "First let's print the whole file:\n"
print_where(current_file)
print_all(current_file)
print_where(current_file)

print "Now let's rewind, kind of like a tape."

rewind (current_file)
print_where(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
print_where(current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
print_where(current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
print_where(current_file)

print "Seeking to 44 in file, truncating, then printing"
current_file.seek(44)
print_where(current_file)
#current_file.truncate()
print_all(current_file)
