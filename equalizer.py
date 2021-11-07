import pyautogui
import time
import pyperclip

## All notes

C1 = 32.70320
CS1 = 34.64783
D1 = 36.70810
DS1 = 38.89087
E1 = 41.20344
F1 = 43.65353
FS1 = 46.24930
G1 = 48.99943
GS1 = 51.91309
A1 = 55.00000
AS1 = 58.27047
B1 = 61.73541

## pyautogui pause between two actions
pyautogui.PAUSE = 0.33

## Get octaves from a base frequency
## Ex: get A4 using getOctave(A1, 4) = 440
def getOctave(frequency, n):
    return frequency * 2 ** (n-1)

## Find cuts between frequencies
def equalizer(listFrequency):
    listFrequency = list(dict.fromkeys(listFrequency))
    listFrequency.sort()
    cuts = []
    for i in range(len(listFrequency)):
        if i + 1 >= len(listFrequency):
            break
        cuts.append((listFrequency[i] + listFrequency[i+1])/2)
    return cuts

##  Auto x,y points in Fabfilter pro Q3
## Use getMouseXY() to unsure posX and posY are correct
def autoFabFilterQ3(frequencies):
    for i in range(len(frequencies)):
        posX = -1125
        posY = 301
        pyautogui.click(x=posX+20*i, y=posY,clicks = 2)
        pyautogui.click(x=posX+20*i, y=posY,clicks = 2)
        pyautogui.write(str(frequencies[i]))
        pyautogui.press('enter')

## Get current position of the mouse 
def getMouseXY(secondsDelay):
    time.sleep(secondsDelay)
    print(pyautogui.position())

#Calling the functions
cuts = equalizer([100,474,390,303,996,1700,3100,216,566,5100])
print(cuts)
autoFabFilterQ3(cuts)







