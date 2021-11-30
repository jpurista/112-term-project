import math, random
import other, intro, game, scores, nav
from cmu_112_graphics import *

# Comment instructions:
        # TODO todo makes it orange
        # ? question mark makes it blue
        # * asterisk makes it green
        # BUG makes first word pink

def appStarted(app):
                app.widthConst = 2 * app.width // 3
                app.heightConst = app.height // 2
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

                app.totalScore, app.levelScore, app.level = 0, 0, 0
                app.structures = [
                        [app.width // 2, app.heightConst + 20, app.widthConst + 120, app.heightConst + 10]
                ]

                if app.level == 0:
                        app.pigLoc = []

                app.username = ''

	# These variables used more globally
                app.results = scores.readScores()
                app.splashScreen = True
                app.gameScreen = False
                app.showScore = False
                app.instruct = False
                app.gameInstruct = False
                app.activeSplash = True
                app.startGame = False
                app.build = False
                app.openLevel = False
                app.end = False
                app.move = True
                app.levelChange = False
                app.endScreen = False

                app.scoreMultiplier = 1
                app.timerDelay = 35

        # X and Y position at different points and different situations
                app.birdX = (app.width // 5) - 15
                app.birdY = app.heightConst
                app.birdXClicked = 0
                app.birdYClicked = 0
                app.birdXReleased = 0
                app.birdYReleased = 0

                app.angleFired = 0


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
        if app.startGame:
                app.move = False
        app.birdX = event.x
        app.birdY = event.y

def mouseReleased(app, event):
        if app.startGame:
                app.move = True
        app.birdXReleased = event.x
        app.birdYReleased = event.y
        app.angleFired = other.roundHalfDown(app.birdYClicked-app.birdYReleased)

def timerFired(app):
        if app.gameScreen:
                other.gameNotActive(app)

        if app.startGame and app.level <= 4:
                app.scoreMultiplier += app.timerDelay*10

        if app.pigLoc == []:
                if app.level >= 4 and app.end == True:
                        app.end = False
                        app.username = app.getUserInput('What is your username?')
                        app.showMessage(f'You finished the pre-built levels!\n {app.username}, you scored: {other.roundHalfDown(1/(app.totalScore*(1/app.scoreMultiplier)))}')
                        scores.writeScores(app, app.username, other.roundHalfDown(1/(app.totalScore*(1/app.scoreMultiplier))))
                        other.gameNotActive(app)
                        app.splashScreen = True
                elif app.level < 4 and app.end == False:
                        app.levelChange = True
                        app.level += 1
                        app.levelScore = 0

        if app.level == 1 and app.levelChange:
                app.levelChange = False
                app.pigLoc = [
                        [app.widthConst + 40, 0 - 50, app.widthConst + 80, 0 - 10],
                        [app.widthConst - 80, 0 - 50, app.widthConst - 40, 0 - 10],
                        [app.widthConst - 20, 0 - 50, app.widthConst + 20, 0 - 10],
                        [app.widthConst - 50, 0 - 90, app.widthConst - 10, 0 - 50],
                        [app.widthConst + 10, 0 - 90, app.widthConst + 50, 0 - 50]
                ]
        if app.level == 2  and app.levelChange:
                app.levelChange = False
                app.pigLoc = [
                        [app.widthConst + 40, 0 - 50, app.widthConst + 80, 0 - 10],
                        [app.widthConst - 80, 0 - 50, app.widthConst - 40, 0 - 10],
                        [app.widthConst - 20, 0 - 50, app.widthConst + 20, 0 - 10]
                ]
        if app.level == 3 and app.levelChange:
                app.levelChange = False
                app.pigLoc = [
                        [app.widthConst + 40, 0 - 50, app.widthConst + 80, 0 - 10],
                        [app.widthConst - 80, 0 - 50, app.widthConst - 40, 0 - 10],
                        [app.widthConst - 20, 0 - 50, app.widthConst + 20, 0 - 10]
                ]
        if app.level == 4 and app.levelChange:
                app.levelChange = False
                app.pigLoc = [
                        [app.widthConst + 40, 0 - 50, app.widthConst + 80, 0 - 10],
                        [app.widthConst - 80, 0 - 50, app.widthConst - 40, 0 - 10],
                        [app.widthConst - 20, 0 - 50, app.widthConst + 20, 0 - 10]
                ]
                app.end = True

        if app.birdX < app.width and app.birdX > 0 and app.birdY > 0 and (app.birdY + 10 ) < (2 * app.height // 3) and app.move:
                game.launcher(app)

        #makes pigs fall as long as they don't touch the structures
        for i in range(len(app.pigLoc)):
                if (app.pigLoc[i][3] < app.heightConst + 10):
                        app.pigLoc[i][1] += 5
                        app.pigLoc[i][3] += 5

        # checks if bird is in area of the pig circles
        for i in range(len(app.pigLoc)):
                if (app.pigLoc[i][0] < app.birdX < app.pigLoc[i][2]) and (app.pigLoc[i][1] < app.birdY < app.pigLoc[i][3]):
                        app.levelScore += 1
                        app.totalScore += 1
                        app.pigLoc.pop(i)
                        break
        
        #random amount that the clouds move from left to right
        app.cloud1X += random.uniform(0.8,1.2)
        app.cloud2X += random.uniform(0.25,0.75)
        app.cloud3X += random.uniform(0.5,1)
        app.cloud4X += random.uniform(0.5,0.75)
        #if the clouds are 100 to the right of the width of the window, then the cloud moves back to the left 
        if app.cloud1X - 100 > app.width: app.cloud1X = -100
        if app.cloud2X - 100 > app.width: app.cloud2X = -100
        if app.cloud3X - 100 > app.width: app.cloud3X = -100
        if app.cloud4X - 100 > app.width: app.cloud4X = -100


def redrawAll(app, canvas):
        h = app.height
        w = app.width

        canvas.create_rectangle(0, 0, w, h, fill='deep sky blue')
        canvas.create_image(app.cloud1X, app.cloud1Y, image=ImageTk.PhotoImage(app.cloud1))
        canvas.create_image(app.cloud2X, app.cloud2Y, image=ImageTk.PhotoImage(app.cloud2))
        canvas.create_image(app.cloud3X, app.cloud3Y, image=ImageTk.PhotoImage(app.cloud3))
        canvas.create_image(app.cloud4X, app.cloud4Y, image=ImageTk.PhotoImage(app.cloud4))

        if app.splashScreen:
                intro.splashScreen(app, canvas, app.activeSplash, w, h)
                if app.instruct == True:
                        intro.instruct(app, canvas, w, h)
        if not app.splashScreen:
                other.round_rectangle(canvas, 17, 23, 107, 63,  fill='light slate gray', outline='light slate gray')
                other.round_rectangle(canvas, 20, 20, 110, 60,  fill='#E5E9EE', outline='#E5E9EE')
                #this font from: https://fonts.google.com/specimen/Press+Start+2P
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