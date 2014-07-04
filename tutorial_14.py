#tutorial #14
#one more input method
#tutorials are getting more interesting

from sys import argv

script, user_name = argv
prompt = '-> '
print "Greetings, %s. My name is %s." % (user_name, script)
print "Do you like my name, %s?" % user_name

like = raw_input(prompt)

print "Where do you live, %s?" % user_name

lives = raw_input(prompt)

print "What is the colour of your eyes?"

eye_colour = raw_input(prompt)

print """
So, what do we have?
When I asked you, whether you like my name, you answered \"%r\".
You live in %r.
You have %r eyes.
""" % (like, lives, eye_colour)
