import math, random
import other, intro, game, scores
from cmu_112_graphics import *

# * if app.released is True, then set birdForce, angleFired, app.birdXReleased, app.birdYReleased, 

# Comment instructions:
        # TODO todo makes it orange
        # ? question mark makes it blue
        # * asterisk makes it green
        # BUG makes first word pink

def appStarted(app):
        #load images
                #all images of clouds drawn by me in photoshop
                clouds = ['images/cloud1.png', 'images/cloud2.png', 'images/cloud3.png', 'images/cloud4.png']
                app.cloud1 = app.scaleImage(app.loadImage(clouds[random.randint(0,3)]), 6)
                app.cloud2 = app.scaleImage(app.loadImage(clouds[random.randint(0,3)]), 6)
                app.cloud3 = app.scaleImage(app.loadImage(clouds[random.randint(0,3)]), 6)
                app.cloud4 = app.scaleImage(app.loadImage(clouds[random.randint(0,3)]), 6)
                app.cloud1X, app.cloud1Y = 550, 150
                app.cloud2X, app.cloud2Y = 200, 250
                app.cloud3X, app.cloud3Y = -10, 400
                app.cloud4X, app.cloud4Y = 150, 100

	# These variables used more globally
                app.splashScreen = True
                app.startGame = False
                app.showScore = False
                app.instruct = False
                app.activeSplash = True
                app.pigLoc = [
                        [2 * app.width // 3 - 40, app.height //2 - 40, 2 * app.width // 3 + 40, app.height //2 + 40]
                ]

                app.birdX = (app.width // 5) - 15
                app.birdY = (2 * app.height // 3) - 70

                app.released = False
                app.birdXReleased = (app.width // 5) - 15
                app.birdYReleased = (2 * app.height // 3) - 70

                app.timerDelay = 35
                app.move = True
        # ? variables not used atm (can be collapsed)
                # #other stuff for game.py
                # app.birdTypes = {'normal': 1, 'bomb': 2, 'split': 1.5, 'speed': 2, 'big': 3}
                # app.structureTypes = {'sm-sq': 2, 'md-sq': 3, 'lg-sq': 4, 'sm-rect': 2, 'md-rect': 3, 'sm-tri': 2, 'md-tri': 3}
                # app.structureMaterials = {'wood': 1, 'stone': 2, 'glass': 1.5}

                # # These variable used in game.py
                # app.totalScore, app.levelScore, app.level = 0, 0, 0
                # app.birdsInLevel = game.birdGeneration(app.level, app.birdTypes)
                # app.obstaclesList = game.obstacleGeneration(app.level, app.structureTypes, app.structureMaterials)

def keyPressed(app, event):
        other.input(app, event, 'key')

def mousePressed(app, event):
        other.input(app, event, 'mouse')

def mouseDragged(app, event):
        app.move = False
        app.birdX = event.x
        app.birdY = event.y

def mouseReleased(app, event):
        app.move = True
        app.birdXReleased = event.x
        app.birdYReleased = event.y
        app.angleFired = calculateAngle((app.width // 5) - 15, (2 * app.height // 3) - 70, app.birdXReleased, app.birdYReleased)

def calculateAngle(x1, y1, x2, y2):
        return math.degrees(math.atan2(y2-y1, x1-x2))

def timerFired(app):
        # TODO
        #* physics of launching bird
        if app.birdX < app.width and app.birdX > 0 and app.birdY > 0 and (app.birdY + 10 ) < (2 * app.height // 3) and app.move:
                game.launcher(app)

        #check if bird is in area of the frog circle
        if  app.pigLoc != [] and app.pigLoc[0][0]< app.birdX < app.pigLoc[0][2] and app.pigLoc[0][1]< app.birdY < app.pigLoc[0][3]:
                app.pigLoc.pop()


        app.cloud1X += 1
        app.cloud2X += 0.75
        app.cloud3X += 0.5
        app.cloud4X += 0.5
        # TODO reset clouds to start at width = 0

def redrawAll(app, canvas):
        h = app.height
        w = app.width

        canvas.create_rectangle(0, 0, w, h, fill='deep sky blue')
        canvas.create_image(app.cloud1X, app.cloud1Y, image=ImageTk.PhotoImage(app.cloud1))
        canvas.create_image(app.cloud2X, app.cloud2Y, image=ImageTk.PhotoImage(app.cloud2))
        canvas.create_image(app.cloud3X, app.cloud3Y, image=ImageTk.PhotoImage(app.cloud3))
        canvas.create_image(app.cloud4X, app.cloud4Y, image=ImageTk.PhotoImage(app.cloud4))

        if app.splashScreen:
                intro.splashScreen(app, canvas, app.activeSplash)
                if app.instruct == True:
                        other.round_rectangle(canvas, w // 6, h // 6, 5 * w // 6, 5 * h // 6, fill='#E5E9EE', outline='#E5E9EE')
                        intro.instruct(app, canvas)
        if not app.splashScreen:
                other.round_rectangle(canvas, 17, 23, 107, 63,  fill='light slate gray', outline='light slate gray')
                other.round_rectangle(canvas, 20, 20, 110, 60,  fill='#E5E9EE', outline='#E5E9EE')
                #this font from: https://fonts.google.comapp.timerDelay * /specimen/Press+Start+2P
                canvas.create_text(65, 40, text='∆(h)', font='PressStart2P 15', fill='#424242')
                if app.startGame:
                        game.start(app, canvas, w, h)
                        if app.pigLoc != []:
                                canvas.create_oval(app.pigLoc[0][0], app.pigLoc[0][1], app.pigLoc[0][2], app.pigLoc[0][3], fill='green', outline='green')
                elif app.showScore:
                        scores.show(app, canvas, w, h)

def startUp():
	runApp(width=700, height=500)

startUp()