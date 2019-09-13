from sys import argv

script, filename = argv

#this prints these questions
#print "We're going to erase %r." % filename
#print "If you don't want that, hit CTRL-C (^C)."
#print "If you do want that, hit RETURN."

print "We're going to erase %r." % filename,
"If you don't want that, hit CTRL-C (^C)." 
"If you do want that, hit RETURN."

raw_input("?")


print "Opening the file..."
target = open(filename, 'w')
#truncating means to empty the file
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#this is where you will write 3 lines to be safe in your file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# the \n means it is asking for a new line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
