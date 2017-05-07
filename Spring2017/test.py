#!/usr/bin/python

from gopigo import *
import sys

import atexit
atexit.register(stop)

y = True

while y:

    # Question 1
    print('Solve 4x5= ')
    answer = raw_input()

    if answer == '20':
        print('That is correct!')
        print(' ')
        fwd()
        time.sleep(2)
        stop()
    else:
        print('I am sorry, the correct answer is 20.')
        print(' ')

    # Question 2
    print('Where does the President of the United States live? ')
    answer = raw_input()

    if answer == 'The White House':
        print('That is correct!')
        print(' ')
        fwd()
        time.sleep(2)
        stop()
    else:
        print('I am sorry, tthe correct answer is The White House.')
        print(' ')

    # Question 3
    print('What is the capital of Connecticut? ')
    answer = raw_input() 

    if answer == 'Hartford':
        print('That is correct!')
        print(' ')
        fwd()
        time.sleep(2)
        stop()
    else:
        print('I am sorry, the correct answer is Hartford.')
        print(' ')

    # Question 4
    print('What edible substance do bees make? ')
    answer = raw_input() 

    if answer == 'honey':
        print('That is correct!')
        print(' ')
        fwd()
        time.sleep(2)
        stop()
    else:
        print('I am sorry, the correct answer is honey.')
        print(' ')

    # Question 5
    print('Who was the first President of the United States? ')
    answer = raw_input() 

    if answer == 'George Washington':
        print('That is correct!')
        print(' ')
        fwd()
        time.sleep(2)
        stop()
    else:
        print('I am sorry, the correct answer is George Washington.')
        print(' ')

    y = False
