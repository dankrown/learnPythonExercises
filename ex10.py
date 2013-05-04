from time import sleep

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
sleep(1)
print persian_cat
print backslash_cat
sleep(1)
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\b" % i
	sleep(0.2)
