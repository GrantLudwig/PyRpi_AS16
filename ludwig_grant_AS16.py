# File Name: ludwig_grant_AS16.py
# File Path: /home/ludwigg/Python/PyRpi_AS16/ludwig_grant_AS16.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS16/ludwig_grant_AS16.py

# Grant Ludwig
# 11/20/2019
# AS.16
# Create a classic highscore system

from graphics import *
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO # Raspberry Pi GPIO library

# Define Constants
ROWS = 7
COLS = 5
LEVELS= 3
SPACE = 25
WID = 100
HGT = 100
OFFSET = 100
FIRST_LETTER = "A"
STICK_RIGHT_VALUE = 0.2
STICK_LEFT_VALUE = 0.8
VOLTAGE = 3.3

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
stickMiddle = True

def MoveStick():
    global chan
    global selectedLetter
    global stickMiddle
    if chan.voltage/VOLTAGE < STICK_RIGHT_VALUE:
        if selectedLetter == "Z":
            selectedLetter = "A"
        else:
            ch = bytes(selectedLetter, 'utf-8')
            letter = bytes([ch[0] + 1])
            letter = str(letter)
            selectedLetter = letter[2]
        stickMiddle = False
    elif chan.voltage/VOLTAGE > STICK_LEFT_VALUE:
        if selectedLetter == "A":
            selectedLetter = "Z"
        else:
            ch = bytes(selectedLetter, 'utf-8') 
            letter = bytes([ch[0] - 1])
            letter = str(letter)
            selectedLetter = letter[2]
        stickMiddle = False
        
def StickCentered():
    global stickMiddle
    if chan.voltage/VOLTAGE > STICK_RIGHT_VALUE and chan.voltage/VOLTAGE < STICK_LEFT_VALUE:
        stickMiddle = True
        
def NextLetter(channel):
    global selected
    selected = True
        
# Setup GPIO
GPIO.setwarnings(False) # Ignore warnings
GPIO.setmode(GPIO.BCM) # Use BCM Pin numbering
GPIO.setup(26, GPIO.IN)

GPIO.add_event_detect(26, GPIO.FALLING, callback=NextLetter, bouncetime=300)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

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

try:
    # Main Loop    
    for k in range(LEVELS): # loop to select each letter
        selectedLetter = FIRST_LETTER
        selected = False
        startTime = time.time()
        while not selected:
            if stickMiddle:
                MoveStick()
            StickCentered()
            for i in range(ROWS):
                for j in range(COLS):
                    if letters[selectedLetter][i][j] == 1:
                        digits[k][i][j].setFill('red')
                    else:
                        digits[k][i][j].setFill('black')
            update(30)
            
    # make user push the button one more time to end the program
    selected = False
    while not selected:
        empty = 0
        
except KeyboardInterrupt: 
    # This code runs on a Keyboard Interrupt <CNTRL>+C
    print('\n\n' + 'Program exited on a Keyboard Interrupt' + '\n') 

finally: 
    # This code runs on every exit and sets any used GPIO pins to input mode.
    GPIO.cleanup()        