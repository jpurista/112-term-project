import math, random
import other, intro, game, scores, nav
from cmu_112_graphics import *

# Comment instructions:
        # TODO todo makes it orange
        # ? question mark makes it blue
        # * asterisk makes it green
        # BUG makes first word pink

#altered version from 15-112 homeworks found on cs.cmu.edu/~112
import decimal
def roundHalfDown(d):
        # Round to nearest with ties going towards from zero.
        rounding = decimal.ROUND_HALF_DOWN
        # See other rounding options here:
        # https://docs.python.org/3/library/decimal.html#rounding-modes
        return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

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

                #all of these images are also made by me in photoshop
                # app.pig = app.loadImage('images/pig.png')
                app.pigLoc = [
                        [2 * app.width // 3 - 40, app.height //2 - 40, 2 * app.width // 3 + 40, app.height //2 + 40],
                ]

	# These variables used more globally
                app.splashScreen = True
                app.gameScreen = False
                app.showScore = False
                app.instruct = False
                app.activeSplash = True
                app.startGame = False
                app.build = False
                app.openLevel = False
                app.move = True

                app.timerDelay = 35

        # X and Y position at different points and different situations
                app.birdX = (app.width // 5) - 15
                app.birdY = app.height // 2

                app.birdXClicked = 0
                app.birdYClicked = 0

                app.birdXReleased = 0
                app.birdYReleased = 0

                app.angleFired = 0


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
        if app.gameScreen == True:
                nav.gameNav(app, event, 'key')
        else:
                nav.nav(app, event, 'key')

def mousePressed(app, event):
        app.birdXClicked = event.x
        app.birdYClicked = event.y
        if app.gameScreen == True:
                nav.gameNav(app, event, 'mouse')
        else:
                nav.nav(app, event, 'mouse')

def mouseDragged(app, event):
        app.move = False
        app.birdX = event.x
        app.birdY = event.y

def mouseReleased(app, event):
        app.move = True
        app.birdXReleased = event.x
        app.birdYReleased = event.y
        app.angleFired = roundHalfDown(app.birdYClicked-app.birdYReleased)

def timerFired(app):
        #* physics of launching bird
        if app.birdX < app.width and app.birdX > 0 and app.birdY > 0 and (app.birdY + 10 ) < (2 * app.height // 3) and app.move:
                game.launcher(app)

        #check if bird is in area of the pig circle
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
                if app.gameScreen:
                        nav.gameNavScreen(app, canvas, w, h)
                elif app.showScore:
                        scores.show(app, canvas, w, h)
                elif app.startGame:
                        game.start(app, canvas, w, h)
                elif app.buildLevel:
                        game.build(app, canvas, w, h)
                elif app.openLevel:
                        game.openLevel(app, canvas, w, h)

runApp(width=700, height=500)