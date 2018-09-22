import pygame
from pynput import keyboard
import os
import sys
from win32api import GetSystemMetrics
import win32api


#extra functions start
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
#extra functions end

pygame.init()

display_width = 800
display_height = 450

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('osu! Bongocat by sgosiaco')

icon = pygame.image.load(resource_path('favicon.ico'))
pygame.display.set_icon(icon)

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

x = 0
y = 0

key1_pressed = False
key2_pressed = False

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

key1 = 'x'
key2 = 'a'

#image start

leftpawUpImg = pygame.image.load(resource_path('lup.png')).convert_alpha()
leftpawDownImg = pygame.image.load(resource_path('ldown.png')).convert_alpha()
rightpawLowerRightImg = pygame.image.load(resource_path('HandLR.png')).convert_alpha()
rightpawUpperLeftImg = pygame.image.load(resource_path('HandUL.png')).convert_alpha()
rightpawUpperRightImg = pygame.image.load(resource_path('HandUR.png')).convert_alpha()
rightpawLowerLeftImg = pygame.image.load(resource_path('HandLL.png')).convert_alpha()

tableImg = pygame.image.load(resource_path('table.png')).convert_alpha()
catImg = pygame.image.load(resource_path('base.png')).convert_alpha()

def leftpawUp(x,y):
    gameDisplay.blit(leftpawUpImg, (x,y))
def leftpawDown(x,y):
    gameDisplay.blit(leftpawDownImg, (x,y))
def rightpawLowerRight(x,y):
    gameDisplay.blit(rightpawLowerRightImg, (x,y))
def rightpawUpperLeft(x,y):
    gameDisplay.blit(rightpawUpperLeftImg, (x,y))
def rightpawUpperRight(x,y):
    gameDisplay.blit(rightpawUpperRightImg, (x,y))
def rightpawLowerLeft(x,y):
    gameDisplay.blit(rightpawLowerLeftImg, (x,y))
def table(x,y):
    gameDisplay.blit(tableImg, (x,y))
def cat(x,y):
    gameDisplay.blit(catImg, (x,y))

#image end

#keyboard start
def on_press(key):
    global key1_pressed
    global key2_pressed
    try:
        if key.char == key1:
            key1_pressed = True
        elif key.char == key2:
            key2_pressed = True
    except AttributeError:
        print('special key {0} pressed'.format(key))
        

def on_release(key):
    global key1_pressed
    global key2_pressed
    try:
        if key.char == key1:
            key1_pressed = False
        elif key.char == key2:
            key2_pressed = False
    except AttributeError:
        print('special key {0} released'.format(key))


key_listener = keyboard. Listener(on_press=on_press, on_release=on_release)
key_listener.start()
#keyboard end

#custom key start
if len(sys.argv) == 3:
    if len(sys.argv[1]) == 1 or len(sys.argv[2]) == 1:
        key1 = sys.argv[1]
        key2 = sys.argv[2]
    else:
        print "Please enter only 1 character for each key!"
        sys.exit()
elif len(sys.argv) != 1:
    print "Usage: "+os.path.basename(__file__)+" {key1} {key2}"
    sys.exit()
#custom key end

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    #mouse start
    mouse_pos_x, mouse_pos_y = win32api.GetCursorPos()
    #mouse end

    gameDisplay.fill(white)
    table(x,y)
    cat(x,y)
    
    #kb control start
    if key1_pressed == True:
        leftpawDown(x,y)
        if key2_pressed == True:
            gameDisplay.fill(white)
            table(x,y)
            cat(x,y)
            leftpawUp(x,y)
    elif key2_pressed == True:
        leftpawDown(x,y)
        if key1_pressed == True:
            gameDisplay.fill(white)
            table(x,y)
            cat(x,y)
            leftpawUp(x,y)
    else:
        leftpawUp(x,y)
    #kb control end
    
    #mouse control start
    if mouse_pos_x < width/2: #left
        if mouse_pos_y < height/2: #top left
            rightpawUpperLeft(x,y)
        else: # bottom right
            rightpawLowerLeft(x,y)
    else: #right
        if mouse_pos_y < height/2: #top right
            rightpawUpperRight(x,y)
        else: # bottom right
            rightpawLowerRight(x,y)
    #mouse control end        

    pygame.display.update()
    clock.tick(30)

key_listener.stop()
pygame.quit()
sys.exit()