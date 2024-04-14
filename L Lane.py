print("Press any Enter to continue...")
input(' ')
print("Continuing execution...")
import pyautogui
import time
import PIL
from PIL import ImageGrab
from PIL import Image
print("Starting")
from pynput.keyboard import Key,Controller
from pyautogui import *

keyboard = Controller()

ReactionTime = 0.1
isPlaying = True

hnCV0=range(250,255)
hnCV1=range(210,230)
hnCV2=range(250,250)

nCV0=range(240,255)
nCV1=range(235,250)
nCV2=range(240,255)

lnCV0=range(160,180)
lnCV1=range(90,110)
lnCV2=range(150,170)

#Overdrive Notes
ohnCV0=range(240,255)
ohnCV1=range(195,220)
ohnCV2=range(190,220)

onCV0=range(120,150)
onCV1=range(10,50)
onCV2=range(0,40)

olnCV0=range(120,150)
olnCV1=range(10,50)
olnCV2=range(0,40)

note = False
holdNote = False

while isPlaying:
#Takes The Screen Shot
    #time.sleep(ReactionTime)
    img = ImageGrab.grab(bbox= ( 1166, 709, 1236, 752), include_layered_windows=False, all_screens=False, xdisplay=None)
    #Image._show(img)
    #Magic aka converting from whatever the pixel colour values are to rgba
    img = img.convert("RGBA")
    datas = img.getdata()

    #Searches for The Magic Colours
    Note = False
    
    for item in datas:
        if item[0] in nCV0 and item[1] in nCV1 and item[2] in nCV2:
            note = True
        elif item[0] in onCV0 and item[1] in onCV1 and item[2] in onCV2:
            note = True


    print('Note='+ str(note) +' holdNote=' + str(holdNote))

    holdNote = False


    if note == True:
        time.sleep(0.1)
        keyDown("l")
        keyUp("l")
        note = False



time.sleep(3)
input('Press Enter To Close')
