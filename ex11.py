#this raw_input will along with the print will ask you a question and allow 
# you to input your answer
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "What is your favorite color?",
favorite_color = raw_input()

#this will print each answer followed by a commma
print "So, you're %r old, %r tall, %r heavy, and %r  favorite color." % (
    age, height, weight,favorite_color)
