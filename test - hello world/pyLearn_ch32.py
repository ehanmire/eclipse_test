# -*- coding: utf-8 -*-

the_count = [1,2,3,4,5]
fruits = ['apple', 'pea', 'orange', 'peach']
change = [1, 'ten cents', 2, 'one dollar', 3, 'five dollars']

for number in the_count:
    print "this number is %d" %number
    
for fruit in fruits:
    print "kinds of fruits: %s" %fruit
    
for i in change:
    print "changes I've got: %s" %i
    
elements = [10]

#for i in range(0,6):
#    print "list에 %d 숫자를 더합니다." %i
#    elements.append(i)
 
elements = range(0,6) # ignore '10'
    
for i in elements:
    print "원소는 %d" %i
    