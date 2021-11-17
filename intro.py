import math, random

def splashScreen(app, canvas):
        w = app.width
        h = app.height
        canvas.create_text(w // 2, h // 3, text='Furious Fowl', font='PressStart2P 30', fill='black')


        canvas.create_rectangle((w // 3)-1, (h // 3) + 56, (2 * w// 3)-1, (h // 3) + 96, fill='light slate gray', outline='light slate gray')
        canvas.create_rectangle((w // 3)-1, (h // 3) + 108, (2 * w// 3)-1, (h // 3) + 148, fill='light slate gray', outline='light slate gray')

        canvas.create_rectangle((w // 3)+2, (h // 3) + 52, (2 * w// 3)+2, (h // 3) + 92, fill='#E5E9EE', outline='#E5E9EE')
        canvas.create_rectangle((w // 3)+2, (h // 3) + 104, (2 * w// 3)+2, (h // 3) + 144, fill='#E5E9EE', outline='#E5E9EE')

        canvas.create_text(w // 2, (h // 3) + 70, text='Play Game', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w // 2, (h // 3) + 120, text='Scoreboard', font='PressStart2P 15', fill='#424242')

def backHome(app, canvas):
        pass