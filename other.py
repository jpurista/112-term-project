import math, random
from cmu_112_graphics import *

# from https://codingshiksha.com/python/python-3-tkinter-drawing-rectangle-with-rounded-corners-on-canvas-window-gui-desktop-app-full-project-for-beginners/
def round_rectangle(canvas, x1, y1, x2, y2, radius=17, **kwargs):
        points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1,
                        x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius,
                        x2, y2-radius, x2, y2, x2-radius, y2, x2-radius, y2,
                        x1+radius, y2, x1+radius, y2, x1, y2, x1, y2-radius,
                        x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)

#altered version from 15-112 homeworks found on cs.cmu.edu/~112
import decimal
def roundHalfDown(d):
        # Round to nearest with ties going towards from zero.
        rounding = decimal.ROUND_HALF_DOWN
        # See other rounding options here:
        # https://docs.python.org/3/library/decimal.html#rounding-modes
        return int(decimal.Decimal(d).to_integral_value(rounding=rounding))