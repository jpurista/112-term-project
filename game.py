import random, math
from cmu_112_graphics import *


def start(gi):

    canvas.create_rectangle(0, 0, w, h, fill='#33C7FF')
    canvas.create_rectangle(0, 2 * h / 3, w, h, fill='#3D9551', outline = '#3D9551')

    def birdGeneration(level):
        allowedScore = level * 3
        result = []
        # each type of bird is worth a different amount of points
        # list of birds that can be used by the player is 'auto-generated'
        options = ['normal', 'bomb', 'mini-split', 'speedster', 'big']
        optionsVal = [1,2,3,4,5]

        # each level is alloted a certain number of points, based on this number
        # each level will get a random list of birds based on their sum of points
        while allowedScore > 0:
            randomNum = random.randint(0, level-1)
            if (allowedScore - optionsVal[randomNum]) >= 0:
                result.append(options[randomNum])
            allowedScore -= optionsVal[randomNum]

        return result

    def obstacleGeneration(level):
        # each possible size and shape along with different materials
        options = ['sm-sq', 'md-sq', 'lg-sq', 'sm-rect', 'md-rect', 'sm-tri', 'md-tri']
        optionsMat= ['wood' , 'stone', 'glass']
        result = []

        if (level < 3): 
            optionsMat = ['wood']
        elif (level > 10): 
            optionsMat.append('metal')

        # this part is similar to the second section of birdGeneration


        return result

    def appStarted(app):
        app.totalScore = 0
        app.levelScore = 0
        app.level = 0

        app.birdsInLevel = birdGeneration(app.level)
        app.obstaclesList = obstacleGeneration(app.level)

        app.birdInMotionX = 0
        app.birdInMotionY = 0

        app.w = app.width
        app.h = app.height

    def mousePressed(app, event):
        if event.x:
            print('mousePressed')

    def timerFired(app):
        #* physics of launching bird is similar to a spring launching an object 
        #* equates to 0.5 * spring constant * (distance pushed back ** 2)
        pass

    def obstaclePieces(app, canvas):
        pass

    def drawLauncher(app, canvas):
        #this doesnt draw the base of the launcher, but rather the slingshot part
        pass

    def drawBird(app,canvas):
        # this only draws the lineup of birds that's beside the launcher
        # this does not include the birds being launched
        canvas.create_rectangle()

    def redrawAll(app, canvas):
        canvas.create_rectangle(app.w // 3, (app.h // 3) + 50, 2 * app.w// 3, (app.h // 3) + 90, fill='red', outline='red')
        canvas.create_rectangle(app.w // 3, (app.h // 3) + 100, 2 * app.w// 3, (app.h // 3) + 140, fill='red', outline='red')
