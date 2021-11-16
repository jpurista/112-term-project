import math, random
import intro, game, scores
from cmu_112_graphics import *

# Comment instructions:
    # TODO todo makes it orange
    # ? question mark makes it blue
    # * asterisk makes it green
    # BUG makes first word pink

def appStarted(app):
	app.h = app.height
	app.w = app.width

def mousePressed(app, event):
	if (app.w // 3 < event.x < 2 * app.w// 3) and ((app.h // 3) + 50 < event.y < (app.h // 3) + 90):
		game.start() #this needs to pass in app, event, AND CANVAS,  but i cant find how to pass in canvas
	elif (app.w // 3 < event.x < 2 * app.w// 3) and ((app.h // 3) + 100 < event.y < (app.h // 3) + 140):
		scores.start() #same with this one
	else:
		print('lmao')

def redrawAll(app, canvas):
	intro.splashScreen(app, canvas)

def startUp():
    runApp(width=600, height=400)

startUp()