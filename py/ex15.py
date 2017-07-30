from sys import argv #function calls

script, filename = argv # assign argv to script and filename

txt = open(filename) # file object 

print "Here's your file %r:" % filename # print
print txt.read() # function txt.read for show the content.

print "Type the filename again:"
file_again = raw_input(">") # user information inputs

txt_again = open(file_again)# "open"function call for file object.

print txt_again.read() # .read()function call for showing the contents.