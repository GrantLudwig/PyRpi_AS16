# 2D List of Objects
# Rich Bankhead

from graphics import *

# Define Constants
ROWS = 7
COLS = 5
LEVELS= 3
SPACE = 25
WID = 100
HGT = 100
OFFSET = 100
FIRST_LETTER = "A"

# Graphics Window Setup
WIN_WIDTH = (WID* COLS)*LEVELS + ((LEVELS+1) * OFFSET) #Pixels
WIN_HEIGHT = (HGT* ROWS) #Pixels
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")


# Dictionary of letters
letters = {"A":((0,0,1,0,0), (0,1,0,1,0), (1,0,0,0,1), (1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1)),
           "B":((1,1,1,1,0), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,0)),
           "C":((1,1,1,1,1), (1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0), (1,1,1,1,1)),
           "D":((1,1,1,1,0), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,0)),
           "E":((1,1,1,1,1), (1,0,0,0,0), (1,0,0,0,0), (1,1,1,1,1), (1,0,0,0,0), (1,0,0,0,0), (1,1,1,1,1)),
           "F":((1,1,1,1,1), (1,0,0,0,0), (1,0,0,0,0), (1,1,1,1,1), (1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0)),
           "G":((1,1,1,1,1), (1,0,0,0,0), (1,0,0,0,0), (1,0,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1)),
           "H":((1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1)),
           "I":((1,1,1,1,1), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (1,1,1,1,1)),
           "J":((0,0,0,0,1), (0,0,0,0,1), (0,0,0,0,1), (0,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1)),
           "K":((1,0,0,0,1), (1,0,0,1,0), (1,0,1,0,0), (1,1,0,0,0), (1,0,1,0,0), (1,0,0,1,0), (1,0,0,0,1)),
           "L":((1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0), (1,1,1,1,1)),
           "M":((1,0,0,0,1), (1,1,0,1,1), (1,0,1,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1)),
           "N":((1,0,0,0,1), (1,1,0,0,1), (1,1,0,0,1), (1,0,1,0,1), (1,0,0,1,1), (1,0,0,1,1), (1,0,0,0,1)),
           "O":((1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1)),
           "P":((1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1), (1,0,0,0,0), (1,0,0,0,0), (1,0,0,0,0)),
           "Q":((1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,1,1), (1,1,1,1,1)),
           "R":((1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1), (1,0,1,0,0), (1,0,0,1,0), (1,0,0,0,1)),
           "S":((1,1,1,1,1), (1,0,0,0,0), (1,0,0,0,0), (1,1,1,1,1), (0,0,0,0,1), (0,0,0,0,1), (1,1,1,1,1)),
           "T":((1,1,1,1,1), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0)),
           "U":((1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1)),
           "V":((1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (0,1,0,1,0), (0,0,1,0,0), (0,0,1,0,0)),
           "W":((1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,1,0,1), (1,0,1,0,1), (1,0,1,0,1), (0,1,0,1,0)),
           "X":((1,0,0,0,1), (0,1,0,1,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,1,0,1,0), (1,0,0,0,1)),
           "Y":((1,0,0,0,1), (0,1,0,1,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0)),
           "Z":((1,1,1,1,1), (0,0,0,0,1), (0,0,0,1,0), (0,0,1,0,0), (0,1,0,0,0), (1,0,0,0,0), (1,1,1,1,1))}
           
selectedLetter = " "
selected = False

def ButtonPress():
    global selectedLetter
    global selected
    keyString = win.checkKey()
    if keyString == "Up":
        if selectedLetter == "Z":
            selectedLetter = "A"
        else:
            ch = bytes(selectedLetter, 'utf-8')
            letter = bytes([ch[0] + 1])
            letter = str(letter)
            selectedLetter = letter[2]
    elif keyString == "Down":
        if selectedLetter == "A":
            selectedLetter = "Z"
        else:
            ch = bytes(selectedLetter, 'utf-8') 
            letter = bytes([ch[0] - 1])
            letter = str(letter)
            selectedLetter = letter[2]
    elif keyString == "space":
        selected = True

# Setup digits
digits = []
for k in range(LEVELS):
	digits.append([])
	for i in range(ROWS):
		digits[k].append([])
		for j in range(COLS):
			digits[k][i].append(Rectangle(Point((k * WID * COLS) + (j * WID) + ((k + 1) * OFFSET), i * HGT), Point((k * WID * COLS) + (j * WID + WID) + ((k + 1) * OFFSET), i * HGT + HGT)))
			digits[k][i][j].draw(win)
			digits[k][i][j].setFill('black')
        
for k in range(LEVELS): # loop to select each letter
    selectedLetter = FIRST_LETTER
    selected = False
    startTime = time.time()
    while not selected:
        ButtonPress()
        for i in range(ROWS):
            for j in range(COLS):
                if letters[selectedLetter][i][j] == 1:
                    digits[k][i][j].setFill('red')
                else:
                    digits[k][i][j].setFill('black')
        update(30)
                    
win.getKey()
win.close()