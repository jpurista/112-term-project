import other, game

def default1(app):
        app.splashScreen, app.showScore, app.startGame, app.buildLevel, app.openLevel = False, False, False, False, False
        app.gameScreen = True

def default2(app):
        app.splashScreen, app.gameScreen, app.startGame, app.buildLevel, app.openLevel = False, False, False, False, False
        app.showScore = True

def default3(app):
        app.gameScreen, app.gameScreen, app.startGame, app.buildLevel, app.openLevel = False, False, False, False, False
        app.splashScreen = True

def default4(app):
        app.splashScreen, app.gameScreen, app.showScore = False, False, False

def nav(app, event, delivery):
        h = app.height
        w = app.width

        if delivery == 'mouse':
                h = app.height
                w = app.width
                if event.x and app.instruct:
                        app.instruct = not app.instruct
                elif (app.splashScreen):
                        if (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 50 < event.y < (h // 3) + 90)  and not app.instruct: #this opens up the game menu
                                default1(app)
                        elif (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 100 < event.y < (h // 3) + 140) and not app.instruct: #this opens up the scores page
                                default2(app)
                        elif (event.x > w - 170) and (event.y > h - 30): #this opens the instructions pop-up
                                app.instruct = True

                if (not app.splashScreen):
                        if (20 < event.x < 110) and (20 < event.y < 60): #takes you back home
                                default3(app)

        elif delivery == 'key':
                if app.splashScreen and not app.instruct:
                        if event.key == 'p':
                                default1(app)
                        elif event.key == 's':
                                default2(app)
                        elif event.key == 'i':
                                app.instruct = True
                else:
                        # ? this is just a quick workaround to reseting the moving circle
                        if event.key == 'r':
                                app.birdX = (app.width // 5) - 15
                                app.birdY = (2 * app.height // 3) - 70
                                app.pigLoc = [[2 * app.width // 3 - 40, app.height //2 - 40, 2 * app.width // 3 + 40, app.height //2 + 40],[1,2,3,4]]
                        ########################
                        if app.instruct and event.key:
                                app.instruct = False
                        if event.key == 'h':
                                default3(app)

def gameNavScreen(app, canvas, w, h):
        #* this is for further gui expansion with options to play a pre-built level, build your own, and open a saved level

        canvas.create_text(w // 2, h // 4, text='Play Game', font='PressStart2P 24', fill='black')
        other.round_rectangle(canvas, (w // 4) - 2, (h // 3) + 56, (3 * w// 4) -2, (h // 3) + 96, fill='light slate gray', outline='light slate gray')
        other.round_rectangle(canvas, (w // 4) - 4, (h // 3) + 108, (2 * w// 4) -4, (h // 3) + 148, fill='light slate gray', outline='light slate gray')
        other.round_rectangle(canvas, (2 * w // 4)+2, (h // 3) + 108, (3 * w// 4)+2, (h // 3) + 148, fill='light slate gray', outline='light slate gray')

        other.round_rectangle(canvas, (w // 4) + 2, (h // 3) + 52, (3 * w// 4)+2, (h // 3) + 92, fill='#E5E9EE', outline='#E5E9EE')
        other.round_rectangle(canvas, (w // 4) , (h // 3) + 104, (2 * w// 4), (h // 3) + 144, fill='#E5E9EE', outline='#E5E9EE')
        other.round_rectangle(canvas, (2 * w // 4)  + 4, (h // 3) + 104, (3 * w// 4) +4, (h // 3) + 144, fill='#E5E9EE', outline='#E5E9EE')

        canvas.create_text(w // 2, (h // 3) + 72, text='Play Pre-Built(p)', font='PressStart2P 15', fill='#424242')
        canvas.create_text(3 * w // 8, (h // 3) + 124, text='Build(b)', font='PressStart2P 15', fill='#424242')
        canvas.create_text(5 * w // 8, (h // 3) + 124, text='Open(o)', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w - 90, h - 20, text='instructions(i)', font='PressStart2P 10', fill='#424242')

        if app.gameInstruct == True:
                game.instruct(app, canvas)

def gameNav(app, event, delivery):
        h = app.height
        w = app.width

        if delivery == 'mouse':
                if event.x and app.gameInstruct:
                        app.gameInstruct = False
                elif not app.splashScreen and (20 < event.x < 110) and (20 < event.y < 60): #this takes you back home
                       default3(app)
                elif ((w // 4) - 2 < event.x <  (3 * w// 4) + 2) and ((h // 3) + 52 < event.y < (h // 3) + 96): #this is for play pre-built game
                        default4(app)
                        app.startGame = True
                elif ((w // 4) -2 < event.x < (2 * w// 4)) and ((h // 3) + 104 < event.y < (h // 3) + 148): #this is for build
                        default4(app)
                        app.buildLevel = True
                elif ((2 * w // 4) - 4 < event.x < (3 * w// 4) +4) and ((h // 3) + 104 < event.y < (h // 3) + 148): #this is for open level
                        default4(app)
                        app.openLevel = True
                elif (event.x > w - 170) and (event.y > h - 30): #this opens the instructions pop-up
                        app.gameInstruct = True
        elif delivery == 'key':
                if app.gameInstruct and event.key:
                        app.gameInstruct = False
                elif event.key == 'h':
                        default3(app)
                elif event.key == 'p':
                        default4(app)
                        app.startGame = True
                elif event.key == 'b':
                        default4(app)
                        app.buildLevel = True
                elif event.key == 'o':
                        default4(app)
                        app.openLevel = True
                elif event.key == 'i':
                        app.gameInstruct = True