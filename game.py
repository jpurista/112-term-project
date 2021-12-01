import math
import other, nav
from cmu_112_graphics import *
'''
this file contains the basis for the actual code such as:
        - startup of different modes
                - start, build
        - read/write/interpret csv files for user-built levels
                - saveLevel, openLevel, redrawCustom, runLevel
        - manage level progression for pre-built levels
                - levelBuildSwitch
        - show instructions
                - instruct
        - manage movement of the bird projectile
                - launcher
'''

def start(app, canvas, w, h):
        other.round_rectangle(canvas, 45, 75, app.width//6 + 30, 2*app.height//3 - 15, fill='light sky blue')
        if app.birdType == 'red':
                canvas.create_oval(app.birdX-10, app.birdY-10, app.birdX+10, app.birdY+10, fill='red', outline='red')
        if app.birdType == 'bigRed':
                canvas.create_oval(app.birdX-20, app.birdY-20, app.birdX+20, app.birdY+20, fill='red', outline='red')
        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green')

        if app.gameMode == 'pre':
                canvas.create_text(app.width // 2, app.height // 8, text = f'level: {app.level}', font='PressStart2P 15', fill='black')
                canvas.create_text(app.width // 2, app.height // 8 + 20, text = f' level score: {app.levelScore}', font='PressStart2P 15', fill='black')
                canvas.create_text(app.width // 2, app.height // 8 + 40, text = f'total score: {app.totalScore}', font='PressStart2P 15', fill='black')
        elif app.gameMode == 'user':
                canvas.create_text(app.width // 2, app.height // 8, text = f'custom level', font='PressStart2P 15', fill='black')

        for i in range(len(app.pigLoc)):
                canvas.create_oval(app.pigLoc[i][0], app.pigLoc[i][1], app.pigLoc[i][2], app.pigLoc[i][3], fill='green', outline='green')
        for i in range(len(app.structures)):
                other.round_rectangle(canvas, app.structures[i][0], app.structures[i][1], app.structures[i][2], app.structures[i][3], fill='gray', outline='dimgray')

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

        canvas.create_line(50, 2*app.height//3, app.width-50, 2*app.height//3 +5, fill = 'red')
        canvas.create_text(app.width //2, 2*app.height//3 + 15, text='anything under this line will not show up when played', font='PressStart2P 10', fill='red')
        canvas.create_oval(app.curPieceX-10, app.curPieceY-10, app.curPieceX+10, app.curPieceY+10, fill='purple', outline='red')
        redrawCustom(app, canvas, app.buildPigLoc, app.buildStructures, 'build')

def runLevel(app, canvas, w, h, pigs, structs):
        other.round_rectangle(canvas, 45, 75, app.width//6 + 30, 2*app.height//3 - 15, fill='light sky blue')
        canvas.create_oval(app.birdX-10, app.birdY-10, app.birdX+10, app.birdY+10, fill='red', outline='red')
        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green')
        canvas.create_text(w // 2, h // 8, text = f'level: {app.level}', font='PressStart2P 15', fill='black')
        canvas.create_text(w // 2, h // 8 + 20, text = f' level score: {app.levelScore}', font='PressStart2P 15', fill='black')
        canvas.create_text(w // 2, h // 8 + 40, text = f'total score: {app.totalScore}', font='PressStart2P 15', fill='black')
        redrawCustom(app, canvas, pigs, structs, 'run')
        app.ballMove = True

def redrawCustom(app, canvas, pigs, structs, comesfrom):
        if comesfrom == 'build':
                for i in range(len(pigs)):
                        canvas.create_oval(pigs[i][1], pigs[i][2], pigs[i][3], pigs[i][4], fill='green', outline='green')
                for i in range(len(structs)):
                        other.round_rectangle(canvas, structs[i][1], structs[i][2], structs[i][3], structs[i][4], fill='gray', outline='dimgray')
        else:
                for i in range(len(pigs)):
                        canvas.create_oval(pigs[i][0], pigs[i][1], pigs[i][2], pigs[i][3], fill='green', outline='green')
                for i in range(len(structs)):
                        other.round_rectangle(canvas, structs[i][0], structs[i][1], structs[i][2], structs[i][3], fill='gray', outline='dimgray')

def launcher(app):
        multiplier = 1
        if app.startGame and  app.ballMove == True:
                if app.birdXReleased < app.birdXClicked:
                        multiplier = -1
                if app.angleFired <= 8:
                        app.angleFired /= 1.05
                app.birdX += 5
                if app.angleFired < 0:
                        app.birdY += multiplier * math.sqrt(abs(app.angleFired))
                else:
                        app.birdY -= multiplier * math.sqrt(app.angleFired)

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

#got help from https://www.w3schools.com/python/python_file_write.asp for read/write functions
def saveLevel(app):
        saveThis = []
        for item in app.buildPigLoc:
                saveThis.append(item)
        for item in app.buildStructures:
                saveThis.append(item)
        filename = app.getUserInput('what filename would you like this to be called?')
        if '.csv' not in filename:
                filename += '.csv'
        userLevel = open(f'userLevels/{filename}', 'x')
        for item in saveThis:
                userLevel.write(f'{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}\n')
        userLevel.close()
        app.showMessage(f'you have successfully saved your file under the name\'{filename}\'.\nTo open/play your level, type \'{filename}\' into the open page.')
        nav.default3(app)
        app.buildPigLoc = []
        app.buildStructures = []

def openLevel(filename):
        if '.csv' not in filename:
                filename += '.csv'
        openedFile = open(f'userLevels/{filename}', 'r')
        result = [[],[]]
        for line in openedFile:
                words = line.split(',')
                if 'Pig' in words[0]:
                        result[0].append([float(words[1]), float(words[2]), float(words[3]), float(words[4])])
                else:
                        result[1].append([float(words[1]), float(words[2]), float(words[3]), float(words[4])])
        return (result[0], result[1])

def levelBuildSwitch(app):
        if app.gameMode == 'pre':
                if app.level == 1 and app.levelChange:
                        app.levelScore = 0
                        app.levelChange = False
                        app.pigLoc = [
                                        [app.widthConst - 80, 0 - 50, app.widthConst - 40, 0 - 10],#bottom left
                                        [app.widthConst - 20, 0 - 50, app.widthConst + 20, 0 - 10],#bottom middle
                                        [app.widthConst + 40, 0 - 50, app.widthConst + 80, 0 - 10],#bottom right
                                ]
                        app.structures = [
                                        [app.width // 2, app.heightConst  + 10, app.widthConst + 120, app.heightConst + 35],
                                ]
                        
                elif app.level == 2  and app.levelChange:
                        app.levelScore = 0
                        app.levelChange = False
                        app.pigLoc = [
                                        [app.widthConst - 80, - 50, app.widthConst - 40, - 10],#bottom left
                                        [app.widthConst - 20, - 50, app.widthConst + 20, - 10],#bottom middle
                                        [app.widthConst + 40, - 50, app.widthConst + 80, - 10],#bottom right
                                        [3 * app.width // 4 + 70, - 50, 3 * app.width // 4 + 110, - 10],#bottom right
                                ]
                        app.structures = [
                                        [app.width // 2, app.heightConst  + 10, app.widthConst + 100, app.heightConst + 35],
                                        [3 * app.width // 4 + 60, app.heightConst  - 20, 3 * app.width // 4 + 120, app.heightConst + 5],
                                ]
                                
                elif app.level == 3 and app.levelChange:
                        app.levelScore = 0
                        app.levelChange = False
                        app.pigLoc = [
                                        [app.widthConst - 80, app.height//4 - 40, app.widthConst - 40, app.height//4],#bottom left
                                        [app.widthConst - 20, app.height//4 - 40, app.widthConst + 20, app.height//4],#bottom middle
                                        [app.widthConst + 40, app.height//4 - 40, app.widthConst + 80, app.height//4],#bottom right
                                        [3 * app.width // 4 + 70, -50, 3 * app.width // 4 + 110, - 10],#other right
                                        [app.width // 3 , -200, app.width //3 + 40, -160],#vertical
                                ]
                        app.structures = [
                                        [app.width // 2, app.heightConst  + 10, app.widthConst + 100, app.heightConst + 35],#longer
                                        [3 * app.width // 4 + 60, app.heightConst  - 20, 3 * app.width // 4 + 120, app.heightConst + 5],#shorter
                                        [app.width //3 - 30, app.height // 3,app.width //3 + 60, app.height // 3+25]# vertical
                                ]

                elif app.level == 4 and app.levelChange:
                        app.levelScore = 0
                        app.levelChange = False
                        app.pigLoc = [
                                        [app.widthConst - 80, app.height//4 - 40, app.widthConst - 40, app.height//4],#bottom left
                                        [app.widthConst - 20, app.height//4 - 40, app.widthConst + 20, app.height//4],#bottom middle
                                        [app.widthConst + 40, app.height//4 - 40, app.widthConst + 80, app.height//4],#bottom right
                                        [3 * app.width // 4 + 70, -50, 3 * app.width // 4 + 110, - 10],#other right
                                        [app.width //3 , -200, app.width //3 + 40, -160],
                                        [app.width //3 + 40 , 2 *app.height // 3 - 40, app.width //3 + 80, 2 * app.height // 3],
                                ]
                        app.structures = [
                                        [app.width // 2, app.heightConst  + 10, app.widthConst + 100, app.heightConst + 35],#longer
                                        [3 * app.width // 4 + 60, app.heightConst  - 20, 3 * app.width // 4 + 120, app.heightConst + 5],#shorter
                                        [app.width //3 - 30, app.height // 3,app.width //3 + 60, app.height // 3+25]# vertical
                                ]
                else:
                        app.end = True