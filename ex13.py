from sys import argv

script, first, second, third = argv

try:
	print "The script is called:", script
	print "Your first variable is:", first
	print "Your second variable is:", second
	print "Your third variable is:", third
except ValueError:
	print "Invalid Arguments use more than 3"
else:
	print "GOOD JOB!"