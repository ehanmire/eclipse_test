# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "%r " %filename
print "if want to cancel, press CTRL+C"
print "otherwise, press Enter"

raw_input("?")

print "Opening file ..."
target = open(filename, 'w')

print "Clear contents of the file. Good Bye!"
target.truncate()

print "Now, I'm going to ask you what you want of three lines to write"

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

print "Then, write them into file"

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

tmp_str = line1+"\n"+line2+"\n"+line3+"\n"
target.write(tmp_str)

print "Finally, close the file"
target.close()