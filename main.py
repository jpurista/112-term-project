import random
import other, intro, game, scores, nav
from cmu_112_graphics import *
'''
this file is the main file for the whole game
it links to all the other files in a (kind of) organized way and manages how they interact with eachother
        - appStarted
                -keeps track of global variables
        - keyPressed, mousePressed, mouseDragged, mouseReleased
                - these track user input for things such as
                        - keystrokes for navigation and naming file
                        - mouse clicks for navigation, actual gameplay, and level creation
        - timerFired
                - functions that are called on constantly
                - refers to other files for some functions like game.launcher
        - redrawAll
                - draws everything through canvas

## refered to in other places, but all images are created by me in photoshop or through tkinter
## however, the font used is from google fonts https://fonts.google.com/specimen/Press+Start+2P
'''

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

# These variables used more globally
        #this reades the scores on the scores.csv files
        app.results = scores.readScores()
        #these jump from start to game menu to score page
        app.splashScreen = True
        app.gameScreen = False
        app.showScore = False
        #these show instructions on start and game menu
        app.instruct = False
        app.gameInstruct = False
        #these are the actions available on the game menu
        app.buildLevel = False
        app.startGame = False
        app.openLevel = False
        app.gameMode = ''
        #this controls the different timing actions in the game
        app.end = False
        app.levelChange = False
        app.endScreen = False
        app.birdType = 'red'

# this stuff is for the level editor/builder
        #this checks which piece we want to add
        app.curPiece = ''
        #this tracks the current X and Y of the piece we have selected
        app.curPieceX = -100
        app.curPieceY = -100
        #this tracks the X and Y of the piece where we released it
        app.curPieceXReleased = -1
        app.curPieceYReleased = -1
        #these lists keep track of pigs and structures (respectively) that were added to the user-built level
        app.buildPigLoc = []
        app.buildStructures = []
        app.released = False
        app.openFilename = ''
        app.curFileName = ''
        app.ballMove = False
        app.lastPiece = []

# X and Y position at different points and different situations
        #these track the curent X and Y of the bird so that it is redrawn in the correct place
        app.birdX = 0
        app.birdY = 0
        #these track where we started and released the bird to caluclate the angle
        app.birdXClicked = 0
        app.birdYClicked = 0
        app.birdXReleased = 0
        app.birdYReleased = 0
        #this is where the angle is stored based on the previous information in the lines above
        app.angleFired = 0

#these are other random variables that I couldnt group into the other categories
        #this is multiplied by the score at the end of the gameScreen
        #it keeps track of time it took to play the game, so longer time is higher score... players want low scores
        app.scoreMultiplier = 1
        #These are the default starting values
        app.totalScore, app.levelScore, app.level = 0, 0, 0
        app.pigLoc = []
        app.structures = []
        #username stored when the player finished playing pre-built leveles
        app.username = ''

def keyPressed(app, event):
        #looks for key presses if on the game menu or level builder
        if app.gameScreen == True or app.buildLevel == True:
                nav.gameNav(app, event, 'key')
        #looks at all other key presses
        else:
                nav.nav(app, event, 'key')

def mousePressed(app, event):
        app.birdXClicked = event.x
        app.birdYClicked = event.y
        #looks for mouse presses if on the game menu or level builder
        if app.gameScreen == True:
                nav.gameNav(app, event, 'mouse')
        elif app.buildLevel == True:
                nav.gameNav(app, event, 'mouse')
                app.ballMove = True
        #looks at all other mouse presses
        elif app.startGame == True:
                nav.gameNav(app, event, 'mouse')
                app.ballMove = True
        else:
                nav.nav(app, event, 'mouse')

def mouseDragged(app, event):
        app.birdX = event.x
        app.birdY = event.y
        #stores the drag position if on the level builder and a piece is selected
        if app.buildLevel == True and app.curPiece != '':
                app.curPieceX = event.x
                app.curPieceY = event.y

def mouseReleased(app, event):
        app.birdXReleased = event.x
        app.birdYReleased = event.y
        #rounds the angle down to the nearest number
        app.angleFired = app.birdYClicked-app.birdYReleased
        #stores the released position if on the level builder and piece is selected
        if app.buildLevel == True and app.curPiece != '':
                app.curPieceXReleased = event.x
                app.curPieceYReleased = event.y

                if 'smallPig' in app.curPiece:
                        app.buildPigLoc.append([app.curPiece, event.x-20, event.y-20, event.x+20, event.y+20])
                elif 'bigPig' in app.curPiece:
                        app.buildPigLoc.append([app.curPiece, event.x-40, event.y-40, event.x+40, event.y+40])
                elif 'longStruct' in app.curPiece:
                        app.buildStructures.append([app.curPiece, event.x-90, event.y, event.x+90, event.y+25])
                elif 'shortStruct' in app.curPiece:
                        app.buildStructures.append([app.curPiece, event.x-12.5, event.y-90, event.x+12.5, event.y+90])

                app.lastPiece.append(app.curPiece)
                app.curPiece = ''
                app.curPieceX = -100
                app.curPieceY = -100

def timerFired(app):
        if app.openFilename != '':
                app.openLevel = True
                app.pigLoc, app.structures= game.openLevel(app.openFilename)
                app.openFilename = ''

        if app.buildLevel == True:
                app.curPieceXReleased = -100
                app.curPieceYReleased = -100
                app.released = False

        #will reset the pre-built game defaults when we are on the game menu
        if app.gameScreen:
                other.gameNotActive(app)

        #this handles the score multiplier based on time
        if app.startGame and app.level <= 4:
                app.scoreMultiplier += 10

        #this will run if there are pigs in the pigLov variable
        if app.pigLoc == []:
                #series of functions to run if we have finished level 4
                #will ask user for username, record score to the scoreboard and scores.csv and opens the splash screen again
                if app.gameMode == 'pre':
                        if app.level >= 4 and app.end == True:
                                app.username = app.getUserInput('What is your username?')
                                if app.username == None: app.username = ' '
                                app.showMessage(f'You finished the pre-built levels!\n {app.username}, you scored: {other.roundHalfDown(1/(app.totalScore*(1/app.scoreMultiplier)))}')
                                scores.writeScores(app, app.username, other.roundHalfDown(1/(app.totalScore*(1/app.scoreMultiplier))))
                                other.gameNotActive(app)
                                nav.default3(app)
                        elif app.level >= 0 and app.levelChange == False:
                                app.level += 1
                                app.birdX = app.width // 8
                                app.birdY = 1.5 * app.height // 4
                                app.ballMove = False
                                app.levelChange = True
                elif app.gameMode == 'user':
                        app.showMessage(f'Great Job!\nYou completed a user-built level.\n The scores for these are not recorded.')
                        other.gameNotActive(app)
                        nav.default3(app)

        #this calls the function in other.py that changes the levels and
        # contains the code for 4 hard-coded levels
        game.levelBuildSwitch(app)

        #TODO check if the bird is touching the structures... if they are, then stop or bounce
        

        #TODO also add so the angle changes 180-angle if it touches one of the structures
        #this doesn't let the bird outside the bounds of the window
        if (app.birdX < app.width and app.birdX > 0) and (app.birdY > 0 and (app.birdY + 10 ) < (2 * app.height // 3)):
                game.launcher(app)

        #TODO change this is it loops through app.structures... only move down if the pigs arent intersecting with the structures
        #makes pigs fall as long if they don't touch the structures
        for struct in app.structures:
                for pig in app.pigLoc:
                        if  pig[3] < 2 * app.height // 3: #stops if the pig touches the ground
                                if pig[3] < struct[1]: #stops if the bottom of the pig touches top of struct
                                        if pig[0] > struct[0] and pig[2] < struct[2]:
                                #stops if the left of the pig is greater than the left of the structure
                                #also stops if right of the pig is greater than the right of the structure
                                                pig[1] += 15
                                                pig[3] += 15

        # checks if bird is in area of the pig circles
        for i in range(len(app.pigLoc)):
                if app.pigLoc[i][1] - 10< app.birdY < app.pigLoc[i][3]+10:
                        if app.pigLoc[i][0] < app.birdX < app.pigLoc[i][2] + 10:
                                app.levelScore += 1
                                app.totalScore += 1
                                app.pigLoc.pop(i)
                                break

        #random amount that the clouds move from left to right
        app.cloud1X += random.uniform(1,2)/2
        app.cloud2X += random.uniform(1,2)/2
        app.cloud3X += random.uniform(1,2)/2
        app.cloud4X += random.uniform(1,2)/2
        #if the clouds are 100 to the right of the width of the window, then the cloud moves back to the left 
        if app.cloud1X - 100 > app.width: app.cloud1X = -100
        if app.cloud2X - 100 > app.width: app.cloud2X = -100
        if app.cloud3X - 100 > app.width: app.cloud3X = -100
        if app.cloud4X - 100 > app.width: app.cloud4X = -100

def redrawAll(app, canvas):
        h = app.height
        w = app.width

        #create constant background no matter what page user is on
        canvas.create_rectangle(0, 0, w, h, fill='deep sky blue')
        canvas.create_image(app.cloud1X, app.cloud1Y, image=ImageTk.PhotoImage(app.cloud1))
        canvas.create_image(app.cloud2X, app.cloud2Y, image=ImageTk.PhotoImage(app.cloud2))
        canvas.create_image(app.cloud3X, app.cloud3Y, image=ImageTk.PhotoImage(app.cloud3))
        canvas.create_image(app.cloud4X, app.cloud4Y, image=ImageTk.PhotoImage(app.cloud4))

        #show the main menu (and instructions if prompted)
        if app.splashScreen:
                intro.splashScreen(app, canvas, True, w, h)
                if app.instruct == True:
                        intro.instruct(app, canvas, w, h)
        if not app.splashScreen:
                #this creates the home button present on every single other page that's not the main menu
                other.round_rectangle(canvas, 17, 23, 107, 63,  fill='light slate gray', outline='light slate gray')
                other.round_rectangle(canvas, 20, 20, 110, 60,  fill='#E5E9EE', outline='#E5E9EE')
                #this font from: https://fonts.google.com/specimen/Press+Start+2P
                canvas.create_text(65, 40, text='∆(h)', font='PressStart2P 15', fill='#424242')
                if app.gameScreen: #show game nav menu if on game menu page
                        nav.gameNavScreen(app, canvas, w, h)
                elif app.showScore: #show the scoreboard if on the scores page
                        scores.show(app, canvas, w, h)
                elif app.startGame: #start the game if playing pre-built levels
                        game.start(app, canvas, w, h)
                elif app.buildLevel: #show the game build interface if on the level builder page
                        game.build(app, canvas, w, h)
                elif app.openLevel: #opens previously built level that's stored in the userLevels folder
                        game.start(app, canvas, w, h)

runApp(width=700, height=500, )