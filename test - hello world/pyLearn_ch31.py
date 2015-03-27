# -*- coding: UTF-8 -*-

print "���� �� ��  �ִ� ��ο� �濡 ���Խ��ϴ�. 1���� 2�� �� �� ��� ������ �����?"

door = raw_input("> ")

if door == "1":
    print "�Ŵ� ���� ġ�� ����ũ�� �԰� �ֽ��ϴ�. ������ �ұ��?"
    print "1. ����ũ�� ���´�."
    print "2. ������ �Ҹ��� ������."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "Head"
    elif bear == "2":
        print "Legs"
    else:
        print "Run"
elif door == "2":
    print "choose 2"
    
else:
    print "done"