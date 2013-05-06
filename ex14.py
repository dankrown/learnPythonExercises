from sys import argv

script, username, password = argv
prompt = '--> '

print " Hi %s, I'm the %s script, this is your password: %s. " % (username, script, password)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % username
likes = raw_input(prompt)

print "Where do you live %s?" % username
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice!!
""" % (likes, lives, computer)
