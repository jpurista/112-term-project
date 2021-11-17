import random, math
import other
from cmu_112_graphics import *

def start(app, canvas, w, h):
        canvas.create_text(w // 2, h // 4, text='This is the game', font='PressStart2P 24', fill='black')
        canvas.create_rectangle(w // 5, 2 * h // 3, (w // 5) + 20, (2 * h // 3) - 60, fill='brown', outline='brown')

def timerFired(app):
        #* physics of launching bird is similar to a spring launching an object 
        #* equates to 0.5 * spring constant * (distance pushed back ** 2)

        pass

def obstaclePieces(app, canvas):
        pass

def drawLauncher(app, canvas):
        #this doesnt draw the base of the launcher, but rather the slingshot part
        pass

def drawBird(app,canvas):
        # this only draws the lineup of birds that's beside the launcher
        # this does not include the birds being launched
        canvas.create_rectangle(0,0,10,10,fill='blue')

def birdGeneration(level):
        allowedScore = level * 2
        result = []
        # each type of bird is worth a different amount of points
        # list of birds that can be used by the player is 'auto-generated'
        options = {'normal': 1, 'bomb': 2, 'mini-split': 1.5, 'speedster': 2, 'big': 3}

        # each level is alloted a certain number of points, based on this number
        # each level will get a random list of birds based on their sum of points
        while allowedScore > 0:
                birdType = random.choice(list(options))
                birdValue = options[birdType]
                if (allowedScore - birdValue) >= 0:
                        result.append(birdType)
                        allowedScore -= birdValue

        return result

def obstacleGeneration(level):
        # each possible size and shape along with different materials
        options = {'sm-sq': 2, 'md-sq': 3, 'lg-sq': 4, 'sm-rect': 2, 'md-rect': 3, 'sm-tri': 2, 'md-tri': 3}
        optionsMat= {'wood': 1, 'stone': 2, 'glass': 1.5}
        allowedScore = level * 3
        result = []

        if (level < 3): 
                optionsMat = {'wood': 1}
        elif (level > 10): 
                optionsMat['metal'] = 3

        # this part is similar to the second section of birdGeneration 

def backHome(app, canvas):
        pass