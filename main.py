import math, random
import intro, game, scores
from cmu_112_graphics import *

# Comment instructions:
        # TODO todo makes it orange
        # ? question mark makes it blue
        # * asterisk makes it green
        # BUG makes first word pink

def appStarted(app):
	# These variables used globally
        app.splashScreen = True
        app.startGame = False
        app.showScore = False
	
	# These variable used in game.py
        app.totalScore, app.levelScore, app.level = 0, 0, 0
        app.birdsInLevel = game.birdGeneration(app.level)
        app.obstaclesList = game.obstacleGeneration(app.level)
        app.birdInMotionX = 0
        app.birdInMotionY = 0

def keyPressed(app, event):
        if event.key == 'Return':
                app.splashScreen = False
                app.startGame = True
                app.showScore = False
        elif event.key == 'h':
                app.splashScreen = False
                app.startGame = False
                app.showScore = True
        elif event.key == 's':
                app.splashScreen = True
                app.startGame = False
                app.showScore = False

def mousePressed(app, event):
        h = app.height
        w = app.width
        if (app.splashScreen):
                if (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 50 < event.y < (h // 3) + 90):
                        app.splashScreen = False
                        app.startGame = True
                        app.showScore = False
                elif (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 100 < event.y < (h // 3) + 140):
                        app.splashScreen = False
                        app.startGame = False
                        app.showScore = True
                else:
                        #add animation of bird where the event.x and event.y is
                        pass
                        
        if (not app.splashScreen):
                if (20 < event.x < 110) and (20 < event.y < 60):
                        app.splashScreen = True
                        app.startGame = False
                        app.showScore = False

def redrawAll(app, canvas):
        h = app.height
        w = app.width
        canvas.create_rectangle(0, 0, w, h, fill='deep sky blue')
        canvas.create_rectangle(0, 2 * h / 3, w, h, fill='green', outline = 'green')
        if app.splashScreen:
                intro.splashScreen(app, canvas)
        if not app.splashScreen:
                canvas.create_rectangle(20, 20, 110, 60, fill='#B5D9FE', outline='#B5D9FE')
                canvas.create_text(65, 40, text='∆Home', font='PressStart2P 15', fill='#424242')
                if app.startGame:
                        game.start(app, canvas, w, h)
                elif app.showScore:
                        scores.show(app, canvas, w, h)

def startUp():
	runApp(width=700, height=500)

startUp()