#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:09:42 2022

@author: monikapatel

A simple pomodoro timer app
import time
"""

import time
import os

def alarm():
    # play sound
    file = "/Users/monikapatel/Projects/Pythonstuff/audio/announcement-sound-21466.mp3"
    #print('playing sound using native player')
    os.system("afplay " + file)

def break_time(break_minutes):
    print('take a break...')
    time.sleep(break_minutes)
    alarm()
    pass

def pomodoro(minutes):
    #pcount = minutes/5
    sleep_time = minutes*60
    print('pomodoro ',minutes,'@',time.strftime("%H:%M"))
    # for i in range(0,sleep_time):
        # time.sleep(1)
    time.sleep(sleep_time)
    
    #mins, secs = divmod(round((time.time()-start),2),60)
    #print('time up','{:2.0f}:{:02.0f}'.format(mins, secs) )
    
    print('time up',time.strftime("%H:%M") )
    alarm()
    #return pcount
    pass



def main_menu():
    print("Enter choice !")
    choice = ''
    counter = 0
    while True:
        choice = input("a- 25 min\nb- 50 min\nc- custom\nq- quit!\n")
        print("choice", choice)
        if(choice =='a'):
            counter += 1
            pomodoro(25)
            break_time(5)
        elif(choice =='b'):
            counter += 2 
            pomodoro(50)
            break_time(10)
        elif(choice == 'c'):
            custom = input('enter minutes (int):')
            counter += custom/25 
            pomodoro(int(custom))
        elif(choice =='q'):
            print('total sessions:','{:.1f}'.format(counter))
            print("bye !")
            break
        else:
            print('invalid choice ohno! :o')
            
    

    
if __name__ == '__main__':
    main_menu()




