# -*- coding: utf-8 -*-

numbers = []

def while_func(count):
    i=0

    while i<count:
        #print "i at the top is %d" %i
        numbers.append(i)
    
        i += 1
    
#    print "Now, numbers are ", numbers
#    print "bottom of i is %d", i

while_func(6)

print "numbers:"

for num in numbers:
    print num
    
