# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephones Light Sugar"

print "we don't have 10 things yet. let's fix it"

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Add: ", next_one
    stuff.append(next_one)
    print "Now %d objs are in the list" % len(stuff)
    
print "let's see!! ", stuff

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print stuff[3:6]
print '#'.join(stuff[3:6])
