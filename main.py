import math, random
from cmu_112_graphics import *

def appStarted(app):
    app.totalScore = 0
    

def timerFired(app):
    pass

def drawObstaclePieces(app,canvas):
    pass

def drawLauncher(app, cavnas):
    pass

def drawBird(app,canvas):
    #physics of launching bird is similar to a spring launching an object
    # equates to 0.5 * spring constant * (distance pushed back ** 2)
    pass

def redrawAll(app, canvas):
    pass

def playFuriousFowl():
    runApp(width=400, height=400)