# -*- coding: utf-8 -*-

def print_two(*args):
    arg1, arg2 = args
    print "실행인자1: %s, 실행인자2: %s" %(arg1, arg2)
    
def print_two_again(arg1, arg2):
    print "실행인자1: %r, 실행인자2: %r" %(arg1, arg2)
    
def print_one(arg1):
    print "실행인자1: %r" %arg1
    
def print_none():
    print "none"
    
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("Zed")
print_none()


