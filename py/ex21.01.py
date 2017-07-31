def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLY %d * %d" % (a, b)
	return a*b
	
def divide(a, b):
	print "DIVIDE %d / %d" % (a, b)
	return a/b
	
	
print "Let's do some math with just functions!"

age = float(raw_input("What's your age? "))
height = float(raw_input("What's your height? "))
weight = int(raw_input("what's your weight? "))
iq = float(raw_input("what's your iq? "))

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "Your current personal sccor is: \n", "*"*30, "\n\t",what, "\n", "*"*30, "\nTrust me, I never lie! \n","*"*30