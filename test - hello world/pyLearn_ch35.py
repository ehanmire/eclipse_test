# -*- coding: utf-8 -*-

from sys import exit

def gold_room():
    print "gold room! how much?"
    
    next = raw_input("> ")
    #if "0" in next or "1" in next:
    #    how_much = int(next)
    #else:
    #    dead("Learn how to write numbers Man!")
    
    if next.int() == True:
        how_much = int(next)
    else:
        dead("Learn how to write numbers Man!")
    
    if how_much < 50:
        print "Good. You win"
        exit(0)
    else:
        dead("Greedy Man")
    
def bear_room():
    print "here is a bear which has honey"
    print "another fat bear stands in front of the other gate"
    print "how would you move bears?"
    
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "steal":
            dead ("A bear hits your head")
        elif next == "tease" and not bear_moved:
            print "Now a bear moved and you can go out"
            bear_moved = True
        elif next == "tease" and bear_moved:
            dead ("Bear gets angry and eat out your leg")
        elif next == "open" and bear_moved:
            gold_room()
        else:
            print "Don't understand"

def cthulhu_room():
    print "In here, we'll call the great deamon, cthulhu"
    print "run? or eat?"
    
    next = raw_input("> ")
    
    if "run" in next:
        start()
    elif "eat" in next:
        dead ("taste good")
    else:
        cthulhu_room()

def dead(why):
    print why, "well Done"
    exit(0)
    
def start():
    print "you are in a dark room"
    print "there are two doors on your left and right"
    print "which one will you choose?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        gold_room()
    else:
        dead ("Starving to death")
        
start()

            