# imports 

import datetime
import random
import math
import tkinter
from tkinter.constants import CENTER


# Initialize GUI 
gui = tkinter.Tk(screenName='Math Quiz')
gui.geometry('1000x1000')
gui.configure(bg='black')

# Functions
def startGame():
    pass

# Adding Buttons
startButton = tkinter.Button(gui, text='Start', width=10, height=3, command=startGame)
startButton.place(relx=.5, rely=.5, anchor=CENTER)

# Game Logic
def gameInCMD():    
    operations = ['+', '-', 'x']
    correct = 0
    incorrect = 0  
    start = datetime.datetime.now()
    limit = 30
    x = 0
    while x < 100:
        pairs = [random.randint(0,12), random.randint(0,12)]
        num1 = pairs[0]
        num2 = pairs[1]
        operator = random.randint(0,2)

        if operator == 0:
            answer = num1 + num2
        elif operator == 1:
            answer = num1 - num2
        else:
            answer = num1 * num2

        input1 = input(str(num1) + ' ' + operations[operator] + ' ' + str(num2) + ' = ')
        
        try:
            if answer == int(input1):
                correct += 1
                print('correct')
            else:
                incorrect += 1
                print('incorrect')
        except:
            incorrect += 1
            print('incorrect')
        
        elapsedTime = (datetime.datetime.now()-start).seconds
        if elapsedTime > limit:
            print("Time is up")
            break

        x += 1
        
    print('Correct: ' + str(correct))
    print('Incorrect: ' + str(incorrect))       
    return correct, incorrect



gameInCMD()

# Main Loop
gui.mainloop()
