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
	
	# These variable used in game.py
        app.totalScore, app.levelScore, app.level = 0, 0, 0
        app.birdsInLevel = game.birdGeneration(app.level)
        app.obstaclesList = game.obstacleGeneration(app.level)
        app.birdInMotionX = 0
        app.birdInMotionY = 0

def keyPressed(app, event):
        if (app.splashScreen) and not app.instruct:
                if event.key == 'p':
                        app.splashScreen = False
                        app.startGame = True
                        app.showScore = False
                elif event.key == 's':
                        app.splashScreen = False
                        app.startGame = False
                        app.showScore = True
                elif event.key == 'i':
                        app.instruct = not app.instruct
        else:
                if event.key == 'h':
                        app.splashScreen = True
                        app.startGame = False
                        app.showScore = False

def mousePressed(app, event):
        h = app.height
        w = app.width
        if event.x and app.instruct:
                app.instruct = not app.instruct
        elif (app.splashScreen):
                if (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 50 < event.y < (h // 3) + 90)  and not app.instruct:
                        app.splashScreen = False
                        app.startGame = True
                        app.showScore = False
                elif (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 100 < event.y < (h // 3) + 140) and not app.instruct:
                        app.splashScreen = False
                        app.startGame = False
                        app.showScore = True
                elif (event.x > w - 170) and (event.y > h - 30):
                        app.instruct = True
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
        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green', tags='notscores')
        if app.splashScreen:
                intro.splashScreen(app, canvas)
                if app.instruct == True:
                        other.round_rectangle(canvas, w // 6, h // 6, 5 * w // 6, 5 * h // 6, fill='#E5E9EE', outline='#E5E9EE')
                        canvas.create_text(w // 2, (h // 6) + 25, text='instructions', font='PressStart2P 15', fill='black')
        if not app.splashScreen:
                other.round_rectangle(canvas, 17, 23, 107, 63,  fill='light slate gray', outline='light slate gray')
                other.round_rectangle(canvas, 20, 20, 110, 60,  fill='#E5E9EE', outline='#E5E9EE')
                canvas.create_text(65, 40, text='∆(h)', font='PressStart2P 15', fill='#424242')
                if app.startGame:
                        game.start(app, canvas, w, h)
                elif app.showScore:
                        canvas.delete("notscores")
                        scores.show(app, canvas, w, h)

def startUp():
	runApp(width=700, height=500)

startUp()