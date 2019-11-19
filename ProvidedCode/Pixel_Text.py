# Pixel Letter Generator
# Generates pixel letters in the form of Dictionaries for Python
# Richard Bankhead 

from graphics import *
import time


#Define Constants
rows = 7
cols = 5
DOT_RAD = 15
OFFSET = 3
BUTTON_RAD = 30
WIN_WIDTH = (DOT_RAD*2 + OFFSET)* cols + OFFSET +  2*OFFSET + BUTTON_RAD *2 + 2*OFFSET #Pixels
WIN_HEIGHT = (DOT_RAD*2+ OFFSET)* rows + OFFSET   #Pixels

win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT)
win.setBackground("grey")

allButtonValue = "red"

#Draw Screen
pixelArray = []
pixelOn = []

for i in range(cols):
    pixelArray.append([])
    pixelOn.append([])
    for j in range(rows):
        pixelArray[i].append(Circle(Point((OFFSET+DOT_RAD*2)*i+OFFSET+DOT_RAD,(OFFSET+DOT_RAD*2)*j+OFFSET+DOT_RAD), DOT_RAD))
        pixelArray[i][j].setFill("black")
        pixelArray[i][j].draw(win)
        pixelOn[i].append(0)
 
#Draw Button
saveButton = Circle(Point((DOT_RAD*2 + OFFSET)* cols + OFFSET + OFFSET+BUTTON_RAD , 2*BUTTON_RAD), BUTTON_RAD)
saveButton.setFill("green")
saveButton.setOutline("black")
saveButton.setWidth(5)
saveButton.draw(win)    

#Draw All Button
allButton = Circle(Point((DOT_RAD*2 + OFFSET)* cols + OFFSET + OFFSET+BUTTON_RAD , 5*BUTTON_RAD), BUTTON_RAD)
allButton.setFill(allButtonValue)
allButton.setOutline("black")
allButton.setWidth(5)
allButton.draw(win) 

      
while True:
    clickPoint = win.checkMouse()
    if clickPoint != None:

        #Check to see if click is on a Ball
        for i in range(cols):
            for j in range(rows):
                if clickPoint.getX() > pixelArray[i][j].getP1().getX() and clickPoint.getX() < pixelArray[i][j].getP2().getX(): 
                    if clickPoint.getY() > pixelArray[i][j].getP1().getY() and clickPoint.getY() < pixelArray[i][j].getP2().getY():
                        if pixelOn[i][j] == 0:
                            pixelOn[i][j] = 1
                            pixelArray[i][j].setFill("red")
                        else:
                            pixelOn[i][j] = 0
                            pixelArray[i][j].setFill("black")

        #Check to see if click is on Export Button
        if clickPoint.getX() > saveButton.getP1().getX() and clickPoint.getX() < saveButton.getP2().getX(): 
            if clickPoint.getY() > saveButton.getP1().getY() and clickPoint.getY() < saveButton.getP2().getY():
                saveButton.setFill("red")
                
                character = input("What character are you creating?:  ")
                
                print("\n\n{\""+character+"\":(", end="")
                for j in range(rows):
                    print("(", end="")
                    
                    for i in range (cols):
                        print(str(pixelOn[i][j]), end="")
                        if i != cols-1:
                            print(',',end="")
                   
                    print(')',end="")
                   
                    if j != rows-1:
                        print(', ',end="")
#                    else:
#                        print('')
                print(")}\n\n")     

                time.sleep(1)
                saveButton.setFill("green")
        
      #Check to see if click is on All Button
        if clickPoint.getX() > allButton.getP1().getX() and clickPoint.getX() < allButton.getP2().getX(): 
            if clickPoint.getY() > allButton.getP1().getY() and clickPoint.getY() < allButton.getP2().getY():
                if allButtonValue == "red":
                    allButtonValue = "black"
                    allButton.setFill(allButtonValue)
                    for i in range(cols):
                        for j in range(rows):
                            pixelOn[i][j] = 1
                            pixelArray[i][j].setFill("red")
                else:
                    allButtonValue = "red"
                    allButton.setFill(allButtonValue)
                    for i in range(cols):
                        for j in range(rows):
                            pixelOn[i][j] = 0
                            pixelArray[i][j].setFill("black")
                    
            

        
