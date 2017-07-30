from sys import argv # module call

script, filename = argv # assign argv to variants

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")# like a trigger

print "Open the file..."
target = open(filename, 'w')# file object

print "Truncating the file,  Goodbay!"
target.truncate()#file truncated

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") #input
line2 = raw_input("line 2: ") #input
line3 = raw_input("line 3: ") #input

print "I'm going to write these to the file."

target.write(line1) # write
target.write("\n") # new line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close() #sorry, still can understand what's the meaning of this sentenc