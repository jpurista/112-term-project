import math, random
import other
from cmu_112_graphics import *

def start(app, canvas, w, h):
        #* this is for further gui expansion with options to play a pre-built level, build your own, and open a saved level
        # canvas.create_text(w // 2, h // 4, text='Play Game', font='PressStart2P 24', fill='black')
        # other.round_rectangle(canvas, (w // 4) - 2, (h // 3) + 56, (3 * w// 4) -2, (h // 3) + 96, fill='light slate gray', outline='light slate gray')
        # other.round_rectangle(canvas, (w // 4) - 4, (h // 3) + 108, (2 * w// 4) -4, (h // 3) + 148, fill='light slate gray', outline='light slate gray')
        # other.round_rectangle(canvas, (2 * w // 4)+2, (h // 3) + 108, (3 * w// 4)+2, (h // 3) + 148, fill='light slate gray', outline='light slate gray')

        # other.round_rectangle(canvas, (w // 4) + 2, (h // 3) + 52, (3 * w// 4)+2, (h // 3) + 92, fill='#E5E9EE', outline='#E5E9EE')
        # other.round_rectangle(canvas, (w // 4) , (h // 3) + 104, (2 * w// 4), (h // 3) + 144, fill='#E5E9EE', outline='#E5E9EE')
        # other.round_rectangle(canvas, (2 * w // 4)  + 4, (h // 3) + 104, (3 * w// 4) +4, (h // 3) + 144, fill='#E5E9EE', outline='#E5E9EE')

        # canvas.create_text(w // 2, (h // 3) + 72, text='Play Pre-Built(p)', font='PressStart2P 15', fill='#424242')
        # canvas.create_text(3 * w // 8, (h // 3) + 124, text='Build(b)', font='PressStart2P 15', fill='#424242')
        # canvas.create_text(5 * w // 8, (h // 3) + 124, text='Open(o)', font='PressStart2P 15', fill='#424242')
        # drawLauncher(app, canvas)

        canvas.create_oval(app.birdX-10, app.birdY-10, app.birdX+10, app.birdY+10, fill='red', outline='red')
        canvas.create_rectangle(0, 2 * h // 3, w, h, fill='green', outline = 'green')
        drawLauncher(app, canvas)
       
       #*example enemy frog

def drawLauncher(app, canvas):
        # TODO this doesnt draw the base of the launcher, but rather the slingshot part
        w = app.width
        h = app.height
        other.round_rectangle(canvas, w // 5, 2 * h // 3, (w // 5) + 15, (2 * h // 3) - 60, fill='brown')

def launcher(app):
        #* force equates to 0.5 * spring constant * (distance pushed back ** 2)
        # * x-component is the horizontal speed
        if (app.birdX, app.birdY) != ((app.width // 5- 15), (2 * app.height // 3 - 70)):
        # * y-component is initialPosition + initialVelocity + 0.5*(neg gravity (-9.8))*time**2
                # birdForce = math.sqrt((((app.width // 5) - 15)-app.birdXReleased)**2 + (((2 * app.height // 3) - 70)-app.birdYReleased)**2)
                # Vy = birdForce * app.angleFired

                app.birdX += 0.5 * app.timerDelay
                app.birdY  +=   (0.5*app.timerDelay) * (app.birdYReleased - ((app.width // 5) - 15)) /  (app.birdXReleased - ((2 * app.height // 3) - 70))
                # (app.width // 5) - 15 + Vy  * math.sin(math.radians(app.angleFired))  - (9.8 * app.timerDelay ** 2) // 2
                
                # print(f'force = {birdForce}')
                print(f'angle = {app.angleFired}')
                print(app.birdX, app.birdY)

def drawBird(app,canvas):
        # TODO this only draws the lineup of birds that's beside the launcher
        # * this does not include the birds being launched
        canvas.create_rectangle(0,0,10,10,fill='blue')

def birdGeneration(level, birdTypes):
        allowedScore = level * 2
        result = []

        # each level is alloted a certain number of points, based on this number
        # each level will get a random list of birds based on their sum of points
        while allowedScore > 1:
                birdType = random.choice(list(birdTypes))
                birdValue = birdTypes[birdType]
                if (allowedScore - birdValue) >= 0:
                        result.append(birdType)
                        allowedScore -= birdValue

        return result

def obstacleGeneration(level, structureType, material):
        # each possible size and shape along with different materials
        allowedScore = level * 3 
        result = []

        if (level < 3): 
                material = {'wood': 1}
        elif (level > 10): 
                material['metal'] = 3

        # TODO this part is  similar to the second section of birdGeneration 
        while allowedScore > 1:
                structType = random.choice(list(type))
                structValue = structureType[structType]
                if (allowedScore - structValue) >= 0:
                        result.append(structType)
                        allowedScore -= structValue
        
        return result

def obstacleCollapse(app, level):
        pass