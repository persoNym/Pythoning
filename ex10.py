import time

tabby_cat = "\tI'm tabbed in."
persion_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persion_cat
print backslash_cat
print fat_cat

try: #try and except statment for loop error
	while True: #endless loop
		for i in ["/","-","|","\\","|"]:
			print "%s\r" % i,
except KeyboardInterrupt:
	print "Loop escaped"
	pass
		