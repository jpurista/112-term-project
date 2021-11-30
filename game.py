import math, random
import other
from cmu_112_graphics import *

def start(app, canvas, w, h):
        other.round_rectangle(canvas, 45, 75, app.width//6 + 30, 2*app.height//3 - 15, fill='light sky blue')
        canvas.create_oval(app.birdX-10, app.birdY-10, app.birdX+10, app.birdY+10, fill='red', outline='red')
        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green')

        canvas.create_text(app.width // 2, app.height // 8, text = f'level: {app.level}', font='PressStart2P 15', fill='black')
        canvas.create_text(app.width // 2, app.height // 8 + 20, text = f' level score: {app.levelScore}', font='PressStart2P 15', fill='black')
        canvas.create_text(app.width // 2, app.height // 8 + 40, text = f'total score: {app.totalScore}', font='PressStart2P 15', fill='black')
        drawPigStruct(app, canvas, app.pigLocs, app.structures)

def drawPigStruct(app, canvas, pigs, structs):
        for i in range(len(pigs)):
                canvas.create_oval(pigs[i][0], pigs[i][1], pigs[i][2], pigs[i][3], fill='green', outline='green')
        for i in range(len(structs)):
                other.round_rectangle(canvas, structs[i][0], structs[i][1], structs[i][2], structs[i][3], fill='gray', outline='dimgray')

def build(app, canvas, w, h):
        other.round_rectangle(canvas, 120, 23, 240, 63,  fill='light slate gray', outline='light slate gray')
        other.round_rectangle(canvas, 123, 20, 243, 60,  fill='#E5E9EE', outline='#E5E9EE')
        #this font from: https://fonts.google.com/specimen/Press+Start+2P
        canvas.create_text(185, 40, text='save(s)', font='PressStart2P 15', fill='#424242')

        other.round_rectangle(canvas, 263, 23, 383, 63,  fill='light slate gray', outline='light slate gray')
        other.round_rectangle(canvas, 266, 20, 386, 60,  fill='#E5E9EE', outline='#E5E9EE')
        canvas.create_text(328, 40, text='undo(u)', font='PressStart2P 15', fill='#424242')

        other.round_rectangle(canvas, app.width // 16, 3 * app.height // 4, 15 * app.width // 16, app.height - 20, fill='#E5E9EE', outline='#E5E9EE')
        other.round_rectangle(canvas, 45, 75, app.width//6 + 30, 2*app.height//3 - 15, fill='light sky blue')
        canvas.create_oval(4 * app.width // 16 - 30, 3.5 * app.height // 4 - 30, 4 * app.width // 16 + 10, 3.5 * app.height // 4 + 10, fill='green', outline='green') # small pig
        canvas.create_oval(6 * app.width // 16 - 50, 3.5 * app.height // 4 - 50, 6 * app.width // 16 + 30, 3.5 * app.height // 4 + 30, fill='green', outline='green') # large pig
        other.round_rectangle(canvas, 8 * app.width // 16 - 30, 3.5 * app.height // 4 - 15, 8 * app.width // 16 + 150, 3.5 * app.height // 4 + 10, fill='gray', outline='dimgray') # long structure
        other.round_rectangle(canvas, 12.5 * app.width // 16 - 10, 3 * app.height // 4 + 15, 12.5 * app.width // 16 + 10, app.height - 35,fill='gray', outline='dimgray') #tall structure

        canvas.create_oval(app.curPieceX-10, app.curPieceY-10, app.curPieceX+10, app.curPieceY+10, fill='blue', outline='red')
        redrawLevel(app, canvas, w, h)


#got help from https://www.w3schools.com/python/python_file_write.asp for read/write functions
def saveLevel(app):
        filename = app.getUserInput('what filename would you like this to be called?')
        userLevel = open(f'userLevels/{filename}.csv', 'x')
        userLevel.write(f'{app.buildPigLocs},{app.buildStructures}')
        # userLevel.write(f'{app.stuff[0]}, {app.stuff[1]}')
        userLevel.close()
        app.stuff = []
        app.splashScreen = True

def openLevel(app, canvas, w, h):
        filename = app.getUserInput('what filename would you like to open (must be exact, also include .csv)')
        openedFile = open(f'userLevels/{filename}', 'r')
        result = []
        for line in openedFile:
                words = line.split('')
                result.append(words)
        #TODO draw every element from the openedFile
        pigs = result[0]
        structs = result[1]
        other.round_rectangle(canvas, 45, 75, app.width//6 + 30, 2*app.height//3 - 15, fill='light sky blue')
        canvas.create_oval(app.birdX-10, app.birdY-10, app.birdX+10, app.birdY+10, fill='red', outline='red')
        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green')

        canvas.create_text(app.width // 2, app.height // 8, text = f'level: {app.level}', font='PressStart2P 15', fill='black')
        canvas.create_text(app.width // 2, app.height // 8 + 20, text = f' level score: {app.levelScore}', font='PressStart2P 15', fill='black')
        canvas.create_text(app.width // 2, app.height // 8 + 40, text = f'total score: {app.totalScore}', font='PressStart2P 15', fill='black')
        drawPigStruct(app, canvas, pigs, structs)

def redrawLevel(app, canvas, w, h):
        for item in app.stuff:
                if 'small' in item[0]:
                        app.buildPigLoc.append([item[1] - 20, item[2] - 20, item[1] + 20, item[2] + 20])
                elif 'big' in item[0]:
                        app.buildPigLoc.append([item[1] - 40, item[2] - 40, item[1] + 40, item[2] + 40])
                elif 'long' in item[0]:
                        app.buildStructures.append([item[1] - 90, item[2] - 12.5, item[1] + 90, item[2] + 12.5])
                else:
                        app.buildStructures.append([item[1] - 12.5, item[2] - 90, item[1] + 12.5, item[2] + 90])
        drawPigStruct(app, canvas, app.buildPigLoc, app.buildStructures)

def launcher(app):
        multiplier = 1
        if app.birdXReleased < app.birdXClicked:
                multiplier = -1
        if app.angleFired <= 8:
                app.angleFired /= 1.1
        for struct in app.structures:
                if app.startGame and (app.birdX, app.birdY) != ((app.width // 5- 15), (2 * app.height // 3 - 70)):
                        app.birdX += 0.5 * app.timerDelay
                        if app.angleFired < 0:
                                app.birdY  +=  multiplier * math.sqrt(0.25 * app.timerDelay * abs(app.angleFired))
                        else:
                                app.birdY  -=  multiplier * math.sqrt(0.25 * app.timerDelay * app.angleFired)
                        
                        if app.birdX == struct[0] and struct[1]:
                                print('break')
                                break

def instruct(app, canvas):
        w = app.width
        h = app.height 
        
        other.round_rectangle(canvas, w // 6, h // 6, 5 * w // 6, 5 * h // 6, fill='#E5E9EE', outline='#E5E9EE')
        #this font from: https://fonts.google.com/specimen/Press+Start+2P
        canvas.create_text(w // 2, h // 6 + 25, text='help', font='PressStart2P 15', fill='black')
        canvas.create_text(w // 6 + 25, h // 6 + 25, text='X', font='PressStart2P 15', fill='black')
        canvas.create_text(w // 2, h // 6 + 100, text='Press the \'play pre-built\'\nbutton or (p) to play. \n', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w // 2, h // 6 + 160, text='Press the \'build\' button\nor (b) to build your\nown level.\n', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w // 2, h // 6 + 225, text='Press the \'open\' button\nor (o) to open a level\nyou previously built.\n', font='PressStart2P 15', fill='#424242')