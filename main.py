import math, random
import intro, game, scores, other
from cmu_112_graphics import *

# Comment instructions:
        # TODO todo makes it orange
        # ? question mark makes it blue
        # * asterisk makes it green
        # BUG makes first word pink

def appStarted(app):
	# These variables used more globally
        app.splashScreen = True
        app.startGame = False
        app.showScore = False
        app.instruct = False
        app.activeSplash = True

        app.angleFired = 45
        # ? variables not used atm (can be collapsed)
                # #other stuff for game.py
                # app.birdTypes = {'normal': 1, 'bomb': 2, 'split': 1.5, 'speed': 2, 'big': 3}
                # app.structureTypes = {'sm-sq': 2, 'md-sq': 3, 'lg-sq': 4, 'sm-rect': 2, 'md-rect': 3, 'sm-tri': 2, 'md-tri': 3}
                # app.structureMaterials = {'wood': 1, 'stone': 2, 'glass': 1.5}

                # # These variable used in game.py
                # app.totalScore, app.levelScore, app.level = 0, 0, 0
                # app.birdsInLevel = game.birdGeneration(app.level, app.birdTypes)
                # app.obstaclesList = game.obstacleGeneration(app.level, app.structureTypes, app.structureMaterials)
        app.birdInMotionX = 0
        app.birdInMotionY = 0

def keyPressed(app, event):
        other.input(app, event, 'key')

def mousePressed(app, event):
        other.input(app, event, 'mouse')

def calculateAngle(x,y):
        return math.degrees(math.atan2(0-y, 0-x))

def timerFired(app):
        # TODO
        #* physics of launching bird is similar to a spring launching an object 
        #* equates to 0.5 * spring constant * (distance pushed back ** 2)
        # if app.startGame and app.birdInMotionX <= app.width and app.birdInMotionY <= app.height:
        #         app.birdInMotionY -= (5 + (app.birdInMotionX * math.tan(app.angleFired)) - 9.8 * (app.birdInMotionX**2) )/ (2 * 5**2 * math.cos(app.angleFired)** 2)
        #         app.birdInMotionX += 10
        #         print(app.birdInMotionX, app.birdInMotionY)
        pass

def redrawAll(app, canvas):
        h = app.height
        w = app.width
        
        canvas.create_rectangle(0, 0, w, h, fill='deep sky blue')
        if app.splashScreen:
                intro.splashScreen(app, canvas, app.activeSplash)
                if app.instruct == True:
                        intro.instruct(app, canvas)
        if not app.splashScreen:
                other.round_rectangle(canvas, 17, 23, 107, 63,  fill='light slate gray', outline='light slate gray')
                other.round_rectangle(canvas, 20, 20, 110, 60,  fill='#E5E9EE', outline='#E5E9EE')
                canvas.create_text(65, 40, text='∆(h)', font='PressStart2P 15', fill='#424242')
                if app.startGame:
                        game.start(app, canvas, w, h)
                        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green')
                elif app.showScore:
                        scores.show(app, canvas, w, h)

def startUp():
	runApp(width=700, height=500)

startUp() 