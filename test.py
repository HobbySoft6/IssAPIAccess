myList = ['oneo', 'six','ten']
str = "one two three four five"
if any(x in str for x in myList):
    print ("Found a match")
else:
    print ("Not a match")