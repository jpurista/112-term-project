import math, random

def splashScreen(app, canvas):
    w = app.width
    h = app.height
    canvas.create_rectangle(0, 0, w, h, fill='#33C7FF')
    canvas.create_rectangle(0, 2 * h / 3, w, h, fill='#3D9551', outline = '#3D9551')
    canvas.create_text(w // 2, h // 3, text='Furious Fowl', font='PressStart2P 30', fill='black', tags='splash')
    canvas.create_rectangle(w // 3, (h // 3) + 50, 2 * w// 3, (h // 3) + 90, fill='#BDACE3', outline='#BDACE3', tags='splash')
    canvas.create_rectangle(w // 3, (h // 3) + 100, 2 * w// 3, (h // 3) + 140, fill='#BDACE3', outline='#BDACE3', tags='splash')

    