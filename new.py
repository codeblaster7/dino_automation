import pyautogui
from PIL import Image , ImageGrab
import time


def hit(key) :
    pyautogui.keyDown ( key )
    return


def isCollide(data) :
    for i in range ( 300 , 415 ) :
        for j in range ( 410 , 563 ) :
            if data[i , j] < 100 :
                hit ( 'down' )
                return
    for i in range ( 300 , 415 ) :
        for j in range ( 563 , 650 ) :
            if data[i , j] < 100 :
                hit ( 'up' )
                return
    return


def takeScreenshot() :
    image = ImageGrab.grab ( ).convert ( 'L' )
    return image


if __name__ == '__main__' :
    print ( "A mangya mokand yel, dino game chalu mad nanag adod ayti😡🤬" )
    time.sleep ( 2 )
    while True :
        image = ImageGrab.grab ( ).convert ( 'L' )
        data = image.load ( )
        if isCollide ( data ) :
            hit ( 'up' )
        '''
        for i in range ( 275 , 345 ) :
            for j in range ( 563 , 650 ) :
                data[i , j] = 0

        for i in range ( 250 , 300 ) :
            for j in range ( 410 , 563 ) :
                data[i , j] = 171
        image.show ( )
        break
        '''
