# this variable equals "there are types of people"
x = "There are %d types of people." % 10
# variable called binary
binary = "binary"
#variable do _not
do_not = "don't"
# variable y adding Binary, do_not where the place holders are
# This where a String is placed inside of a String
y = "Those who know %s and those who %s." % (binary, do_not)

# this will print x variable
print x
#this will print y variable
print y

#this will print string with variable x
# This where a String is placed inside of a String
print "I said: %r." % x
# this will pring string with variable y
# This where a String is placed inside of a String
print  "I also said: '%s'." % y
# will print answer to question
hilarious = False
# will print question
joke_evaluation = "Isn't that joke funny?! %r"
# print together  on the same line question & answer
print joke_evaluation % hilarious
# Variables w & e
w  = "This is the left side of ..."
e  = "a string with a right side."
# prints both variables together
print w + e 
