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
    print('playing sound using native player')
    os.system("afplay " + file)

def pomodoro(minutes):
    start = time.time()
    sleep_time = minutes*60
    print('pomodoro ',minutes)
    # for i in range(0,sleep_time):
        # time.sleep(1)
    time.sleep(sleep_time)
    
    secs_passed = time.time()-start
    mins = secs_passed//60
    secs = secs_passed%60
    #mins, secs = divmod(round((time.time()-start),2),60)
    print('time up','{:2.0f}:{:02.0f}'.format(mins, secs) )
    alarm()
    pass



def main_menu():
    print("Enter choice !")
    choice = ''
    while True:
        choice = input("a- 25 min\nb- 50 min\nc- custom\nq- quit!\n")
        print("choice", choice)
        if(choice =='a'):
            pomodoro(2)
        elif(choice =='b'):
            pomodoro(5)
        elif(choice == 'c'):
            custom = input('enter minutes (int):')
            pomodoro(int(custom))
        elif(choice =='q'):
            print("bye !")
            break
        else:
            print('invalid choice ohno! :o')
            
    

    
if __name__ == '__main__':
    main_menu()




