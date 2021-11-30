import math, random
import other
from cmu_112_graphics import *

def start(app, canvas, w, h):
        other.round_rectangle(canvas, 45, 75, app.width//6 + 30, 2*app.height//3 - 15, fill='light sky blue')
        canvas.create_oval(app.birdX-10, app.birdY-10, app.birdX+10, app.birdY+10, fill='red', outline='red')
        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green')

        canvas.create_text(app.width // 2, app.height // 8, text = f'level :{app.level}', font='PressStart2P 15', fill='black')
        canvas.create_text(app.width // 2, app.height // 8 + 20, text = f' level score :{app.levelScore}', font='PressStart2P 15', fill='black')
        canvas.create_text(app.width // 2, app.height // 8 + 40, text = f'total score: {app.totalScore}', font='PressStart2P 15', fill='black')

        for i in range(len(app.pigLoc)):
                canvas.create_oval(app.pigLoc[i][0], app.pigLoc[i][1], app.pigLoc[i][2], app.pigLoc[i][3], fill='green', outline='green')
        for i in range(len(app.structures)):
                other.round_rectangle(canvas, app.structures[i][0], app.structures[i][1], app.structures[i][2], app.structures[i][3], radius = 0, fill='gray', outline='dimgray')

def build(app, canvas, w, h):
        pass

def openLevel(app, canvas, w, h):
        pass

def launcher(app):
        if app.startGame and (app.birdX, app.birdY) != ((app.width // 5- 15), (2 * app.height // 3 - 70)):
                app.birdX += 0.5 * app.timerDelay

                if app.angleFired <= 8:
                        app.angleFired /= 1.1

                multiplier = 1
                if app.birdXReleased < app.birdXClicked:
                        multiplier = -1

                if app.angleFired < 0:
                        app.birdY  +=  multiplier * math.sqrt(0.25 * app.timerDelay * abs(app.angleFired))
                else:
                        app.birdY  -=  multiplier * math.sqrt(0.25 * app.timerDelay * app.angleFired)

def instruct(app, canvas):
        w = app.width
        h = app.height 
        
        other.round_rectangle(canvas, w // 6, h // 6, 5 * w // 6, 5 * h // 6, fill='#E5E9EE', outline='#E5E9EE')
        canvas.create_text(w // 2, h // 6 + 25, text='help', font='PressStart2P 15', fill='black')
        canvas.create_text(w // 6 + 25, h // 6 + 25, text='X', font='PressStart2P 15', fill='black')
        canvas.create_text(w // 2, h // 6 + 100, text='Press the \'play pre-built\'\nbutton or (p) to play. \n', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w // 2, h // 6 + 160, text='Press the \'build\' button\nor (b) to build your\nown level.\n', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w // 2, h // 6 + 225, text='Press the \'open\' button\nor (o) to open a level\nyou previously built.\n', font='PressStart2P 15', fill='#424242')

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