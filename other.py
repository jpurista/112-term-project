import random, math
from cmu_112_graphics import *

# from https://codingshiksha.com/python/python-3-tkinter-drawing-rectangle-with-rounded-corners-on-canvas-window-gui-desktop-app-full-project-for-beginners/
def round_rectangle(canvas, x1, y1, x2, y2, radius=17, **kwargs):
        points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1,
                        x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius,
                        x2, y2-radius, x2, y2, x2-radius, y2, x2-radius, y2,
                        x1+radius, y2, x1+radius, y2, x1, y2, x1, y2-radius,
                        x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
        return canvas.create_polygon(points, **kwargs)

def input(app, event, delivery):
        h = app.height
        w = app.width

        if delivery == 'mouse':
                h = app.height
                w = app.width
                if event.x and app.instruct:
                        app.instruct = not app.instruct
                elif (app.splashScreen):
                        if (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 50 < event.y < (h // 3) + 90)  and not app.instruct:
                                app.splashScreen = False
                                app.startGame = True
                                app.showScore = False
                                app.birdX = (app.width // 5) - 15
                                app.birdY = (2 * app.height // 3) - 70
                        elif (w // 3 < event.x < 2 * w // 3) and ((h // 3) + 100 < event.y < (h // 3) + 140) and not app.instruct:
                                app.splashScreen = False
                                app.startGame = False
                                app.showScore = True
                        elif (event.x > w - 170) and (event.y > h - 30):
                                app.instruct = True
                        else:
                                print(f'{event.x}, {event.y}')
                        
                if (not app.splashScreen):
                        if (20 < event.x < 110) and (20 < event.y < 60):
                                app.splashScreen = True
                                app.startGame = False
                                app.showScore = False
                
        elif delivery == 'key':
                if app.splashScreen and not app.instruct:
                        if event.key == 'p':
                                app.splashScreen = False
                                app.startGame = True
                                app.showScore = False
                        elif event.key == 's':
                                app.splashScreen = False
                                app.startGame = False
                                app.showScore = True
                        elif event.key == 'i':
                                app.instruct = True
                else:
                        # ? this is just a quick workaround to reseting the moving circle
                        if event.key == 'r':
                                app.birdX = (app.width // 5) - 15
                                app.birdY = (2 * app.height // 3) - 70
                        ########################
                        if app.instruct and event.key:
                                app.instruct = False
                        if event.key == 'h':
                                app.splashScreen = True
                                app.startGame = False
                                app.showScore = False