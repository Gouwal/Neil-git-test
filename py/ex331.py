i = 0
numbers = []

while i<6:
	print "At the top i is %d" % i
	numbers.append(i) # append is like the stack, and always add the latest number into "numbers"
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
#print "The numbers: "
	
#for num in numbers:
#	print num

for i in range(6, 16):
	numbers.append(i)
for num in numbers:
	print "Numbers are : %d" % num