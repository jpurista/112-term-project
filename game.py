import random, math
import other
from cmu_112_graphics import *

def start(app, canvas, w, h):
        canvas.create_text(w // 2, h // 4, text='This is the game', font='PressStart2P 24', fill='black')
        canvas.create_rectangle(w // 5, 2 * h // 3, (w // 5) + 20, (2 * h // 3) - 60, fill='brown', outline='brown')

def timerFired(app):
        # TODO
        #* physics of launching bird is similar to a spring launching an object 
        #* equates to 0.5 * spring constant * (distance pushed back ** 2)

        pass

def obstaclePieces(app, canvas):
        # TODO draw obstacle pieces
        pass

def drawLauncher(app, canvas):
        # TODO this doesnt draw the base of the launcher, but rather the slingshot part
        pass

def drawBird(app,canvas):
        # TODO this only draws the lineup of birds that's beside the launcher
        # * this does not include the birds being launched
        canvas.create_rectangle(0,0,10,10,fill='blue')

def birdGeneration(level, birdTypes):
        allowedScore = level * 2
        result = []

        # each level is alloted a certain number of points, based on this number
        # each level will get a random list of birds based on their sum of points
        while allowedScore > 1:
                birdType = random.choice(list(birdTypes))
                birdValue = birdTypes[birdType]
                if (allowedScore - birdValue) >= 0:
                        result.append(birdType)
                        allowedScore -= birdValue

        return result

def obstacleGeneration(level, type, material):
        # each possible size and shape along with different materials
        allowedScore = level * 3
        result = []

        if (level < 3): 
                material = {'wood': 1}
        elif (level > 10): 
                material['metal'] = 3

        # TODO this part is similar to the second section of birdGeneration 
        while allowedScore > 1:
                structType = random.choice(list(type))
                structValue = type[structType]
                if (allowedScore - structValue) >= 0:
                        result.append(structType)
                        allowedScore -= structValue

def backHome(app, canvas):
        pass