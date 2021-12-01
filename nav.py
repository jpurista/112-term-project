import other, game
'''
this file contains functions that control user navigation through the game
'''

def default1(app): #default when we want to show the game menu
        app.splashScreen, app.showScore, app.startGame, app.buildLevel, app.openLevel = False, False, False, False, False
        app.gameScreen = True

def default2(app): #default when we want to show the scoreboard
        app.splashScreen, app.gameScreen, app.startGame, app.buildLevel, app.openLevel = False, False, False, False, False
        app.showScore = True

def default3(app): #default when we want to show the main menu
        app.showScore, app.gameScreen, app.startGame, app.buildLevel, app.openLevel = False, False, False, False, False
        app.splashScreen = True
        app.ballMove = False

def default4(app): #default when we don't want to show any menus or the scoreboard
        app.splashScreen, app.gameScreen, app.showScore = False, False, False

#navigation for pages that aren't gameplay or level build
def nav(app, event, delivery):
        h = app.height
        w = app.width

        if delivery == 'mouse':
                if event.x and app.instruct:
                        app.instruct = not app.instruct
                elif (20 < event.x < 110) and (20 < event.y < 60): #takes you back home
                        default3(app)
                        other.gameNotActive(app)
                elif app.splashScreen:
                        if (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 50 < event.y < (h // 3) + 90)  and not app.instruct: #this opens up the game menu
                                default1(app)
                        elif (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 100 < event.y < (h // 3) + 140) and not app.instruct: #this opens up the scores page
                                default2(app)
                        elif (event.x > w - 170) and (event.y > h - 30): #this opens the instructions pop-up
                                app.instruct = True
                        
        elif delivery == 'key':
                if app.splashScreen and not app.instruct:
                        if event.key == 'p':
                                default1(app)
                        elif event.key == 's':
                                default2(app)
                        elif event.key == 'i':
                                app.instruct = True
                else:
                        if app.instruct and event.key:
                                app.instruct = False
                        elif event.key == 'h':
                                default3(app)
                                other.gameNotActive(app)

def gameNav(app, event, delivery):
        h = app.height
        w = app.width

        if delivery == 'mouse':
                if event.x and app.gameInstruct:
                        app.gameInstruct = False
                elif (20 < event.x < 110) and (20 < event.y < 60): #takes you back home
                        default3(app)
                        other.gameNotActive(app)
                elif app.buildLevel:
                        if (140 < event.x < 243) and (20 < event.y < 63):
                                game.saveLevel(app)
                        elif (263 < event.x < 366) and (20 < event.y < 63) and app.lastPiece != []:
                                if 'Pig' in app.lastPiece[-1] and app.buildPigLoc != []:
                                        app.buildPigLoc.pop()
                                        app.lastPiece.pop()
                                elif 'Struct' in app.lastPiece[-1] and app.buildStructures != []:
                                        app.buildStructures.pop()
                                        app.lastPiece.pop()
                        elif (4 * app.width // 16 - 30 < event.x < 4 * app.width // 16 + 10) and (3.5 * app.height // 4 - 30 < event.y < 3.5 * app.height // 4 + 10):
                                app.curPiece = 'smallPig'
                                print('small')
                        elif (6 * app.width // 16 - 50 < event.x < 6 * app.width // 16 + 30) and (3.5 * app.height // 4 - 50 < event.y < 3.5 * app.height // 4 + 30):
                                app.curPiece = 'bigPig'
                                print('big')
                        elif (8 * app.width // 16 - 30 < event.x <  8 * app.width // 16 + 150) and (3.5 * app.height // 4 - 15 < event.y< 3.5 * app.height // 4 + 10):
                                app.curPiece = 'longStruct'
                                print('long')
                        elif (12.5 * app.width // 16 - 10 < event.x <  12.5 * app.width // 16 + 10) and (3 * app.height // 4 + 15 < event.y < app.height - 35):
                                app.curPiece = 'shortStruct'
                                print('short')
                elif app.buildLevel == False:
                        if ((w // 4) - 2 < event.x <  (3 * w// 4) + 2) and ((h // 3) + 52 < event.y < (h // 3) + 96): #this is for play pre-built game
                                default4(app)
                                app.gameMode = 'pre'
                                app.startGame = True
                        elif ((w // 4) -2 < event.x < (2 * w// 4)) and ((h // 3) + 104 < event.y < (h // 3) + 148): #this is for build
                                default4(app)
                                app.buildLevel = True
                        elif ((2 * w // 4) - 4 < event.x < (3 * w// 4) +4) and ((h // 3) + 104 < event.y < (h // 3) + 148): #this is for open level
                                default4(app)
                                app.openFilename = app.getUserInput('what filename would you like to open (must be exact, also include .csv)')
                                app.gameMode = 'user'
                                app.startGame = True
                        elif (event.x > w - 170) and (event.y > h - 30): #this opens the instructions pop-up
                                app.gameInstruct = True
        elif delivery == 'key':
                if app.gameInstruct and event.key:
                        app.gameInstruct = False
                elif app.buildLevel:
                        if event.key == 's':
                                game.saveLevel(app)
                        elif event.key == 'u' and app.lastPiece != []:
                                if 'Pig' in app.lastPiece[-1] and app.buildPigLoc != []:
                                        app.buildPigLoc.pop()
                                        app.lastPiece.pop()
                                elif 'Struct' in app.lastPiece[-1] and app.buildStructures != []:
                                        app.buildStructures.pop()
                                        app.lastPiece.pop()
                elif app.buildLevel == False:
                        if event.key == 'h':
                                default3(app)
                                other.gameNotActive(app)
                        elif event.key == 'p':
                                default4(app)
                                app.gameMode = 'pre'
                                app.startGame = True
                        elif event.key == 'b':
                                default4(app)
                                app.buildLevel = True
                        elif event.key == 'o':
                                default4(app)
                                app.openFilename = app.getUserInput('what filename would you like to open (must be exact, also include .csv)')
                                app.gameMode = 'user'
                                app.startGame = True
                        elif event.key == 'i':
                                app.gameInstruct = True
                        elif event.key == 't':
                                if app.birdType == 'red':
                                        app.birdType = 'bigRed'
                                else:
                                        app.birdType = 'red'

def gameNavScreen(app, canvas, w, h):
        #this creates all the buttons on the game navigation menu
        #this font from: https://fonts.google.com/specimen/Press+Start+2P
        canvas.create_text(w // 2, h // 4, text='Play Game', font='PressStart2P 24', fill='black')
        other.round_rectangle(canvas, (w // 4) - 2, (h // 3) + 56, (3 * w// 4) -2, (h // 3) + 96, fill='light slate gray', outline='light slate gray')
        other.round_rectangle(canvas, (w // 4) - 4, (h // 3) + 108, (2 * w// 4) -4, (h // 3) + 148, fill='light slate gray', outline='light slate gray')
        other.round_rectangle(canvas, (2 * w // 4)+2, (h // 3) + 108, (3 * w// 4)+2, (h // 3) + 148, fill='light slate gray', outline='light slate gray')

        other.round_rectangle(canvas, (w // 4) + 2, (h // 3) + 52, (3 * w// 4)+2, (h // 3) + 92, fill='#E5E9EE', outline='#E5E9EE')
        other.round_rectangle(canvas, (w // 4) , (h // 3) + 104, (2 * w// 4), (h // 3) + 144, fill='#E5E9EE', outline='#E5E9EE')
        other.round_rectangle(canvas, (2 * w // 4)  + 4, (h // 3) + 104, (3 * w// 4) +4, (h // 3) + 144, fill='#E5E9EE', outline='#E5E9EE')

        #this font from: https://fonts.google.com/specimen/Press+Start+2P
        canvas.create_text(w // 2, (h // 3) + 72, text='Play Pre-Built(p)', font='PressStart2P 15', fill='#424242')
        canvas.create_text(3 * w // 8, (h // 3) + 124, text='Build(b)', font='PressStart2P 15', fill='#424242')
        canvas.create_text(5 * w // 8, (h // 3) + 124, text='Open(o)', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w - 90, h - 20, text='instructions(i)', font='PressStart2P 10', fill='#424242')

        #this shows the instructions if prompted
        if app.gameInstruct == True:
                game.instruct(app, canvas)