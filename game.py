import math, random
import other
from cmu_112_graphics import *

def start(app, canvas, w, h):
        other.round_rectangle(canvas, 45, 75, app.width//6 + 30, 2*app.height//3 - 15, fill='light sky blue')
        canvas.create_oval(app.birdX-10, app.birdY-10, app.birdX+10, app.birdY+10, fill='red', outline='red')
        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green')
        if app.pigLoc != []:
                canvas.create_oval(app.pigLoc[0][0], app.pigLoc[0][1], app.pigLoc[0][2], app.pigLoc[0][3], fill='green', outline='green')

def build(app, canvas, w, h):
        print('this is the actual print to build the game')

def openLevel(app, canvas, w, h):
        print('this is the actual print to open a user-built level')

def launcher(app):
        if (app.birdX, app.birdY) != ((app.width // 5- 15), (2 * app.height // 3 - 70)):
                app.birdX += 0.5 * app.timerDelay

                if app.angleFired <= 20:
                        app.angleFired /= 1.25

                if app.angleFired < 0:
                        app.birdY  +=  math.sqrt(0.25 * app.timerDelay * abs(app.angleFired))
                else:
                        app.birdY  -=  math.sqrt(0.25 * app.timerDelay * app.angleFired)
                
                print(f'angle = {app.angleFired}')
                print(app.birdX, app.birdY)

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

def obstacleGeneration(level, structureType, material):
        # each possible size and shape along with different materials
        allowedScore = level * 3 
        result = []

        if (level < 3): 
                material = {'wood': 1}
        elif (level > 10): 
                material['metal'] = 3

        # TODO this part is  similar to the second section of birdGeneration 
        while allowedScore > 1:
                structType = random.choice(list(type))
                structValue = structureType[structType]
                if (allowedScore - structValue) >= 0:
                        result.append(structType)
                        allowedScore -= structValue
        
        return result

def obstacleCollapse(app, level):
        pass